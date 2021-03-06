import React from 'react'
import axios from 'axios'
import Map from '../common/map'
const moment = require('moment')
// import M from 'materialize-css'
import { Slider, Slide, Modal, Button } from 'react-materialize'
import { Link } from 'react-router-dom'
import Auth from '../../lib/auth'
import Container from '../common/container'
const filestackkey = process.env.FILESTACK_KEY
import * as filestack from 'filestack-js'
const client = filestack.init(filestackkey)

const checkLikes = function(likes) {
  return likes.id === Auth.getPayload().sub
}

class spotShow extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {}, user: {}, spot: {}, comment: {} }

    this.handleDelete = this.handleDelete.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleImageSubmit = this.handleImageSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.likeButton = this.likeButton.bind(this)
    this.mapCenter = { lat: 51.515, lng: -0.078 }
    this.updateState = this.updateState.bind(this)
    this.openModal = this.openModal.bind(this)
  }

  componentDidMount() {
    this.getThisSpot()
  }

  getThisSpot() {
    axios.get(`/api/spots/${this.props.match.params.id}`)
      .then(res => this.setState({ spot: res.data }))
    axios.get(`/api/users/${Auth.getPayload().sub}`)
      .then(res => this.setState({ data: res.data.user }))
    const { lat, lng } = this.mapCenter
    this.getSpots(lat, lng, 10000)
  }

  getSpots(locationlat, locationlon, radius) {
    axios.get('/api/spots', {
      params: { locationlat, locationlon, radius }
    })
      .then(res => {
        this.setState({ points: res.data })
      })
  }

  handleDelete() {
    axios.delete(`/api/spots/${this.props.match.params.id}`,
      { headers: { Authorization: `Bearer ${Auth.getToken()}`}})
      .then(() => this.props.history.push('/home'))
      .catch(err => console.log(err.message))
  }

  isOwner() {
    return Auth.isAuthenticated() && this.state.spot.creator.id === Auth.getPayload().sub
  }

  isImageOwner(image) {
    return Auth.isAuthenticated() && image === Auth.getPayload().sub
  }

  handleChange({ target: { name, value } }) {
    const comment = {...this.state.comment, [name]: value }
    const errors = {...this.state.errors, [name]: null }
    this.setState({ comment, errors })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post(`/api/spots/${this.props.match.params.id}/comments`,
      this.state.comment,
      { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
      .then((res) => {
        if (res.data.errors) {
          this.setState({ sent: 'false' })
        } else {
          this.setState({ sent: 'true', comment: {} })
          this.getThisSpot()
        }
      })
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  likeButton() {
    axios.put(`/api/spots/${this.props.match.params.id}/like`,
      this.state.comment,
      { headers: {Authorization: `Bearer ${Auth.getToken()}`}})
      .then((res) => {
        if (res.data.errors) {
          this.setState({ sent: 'false' })
        } else {
          this.setState({ sent: 'true', comment: {} })
          this.getThisSpot()
        }
      })
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  handleImageSubmit() {
    axios({
      url: `/api/spots/${this.props.match.params.id}/images`,
      method: 'POST',
      headers: {Authorization: `Bearer ${Auth.getToken()}`},
      data: {
        path: this.state.image
      },
      json: true
    })
      .then(() => {
        this.getThisSpot()
        this.setState({ sent: 'true', comment: {} })
        document.location.reload(true)
      })
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  deleteImage(imageId) {
    axios({
      url: `/api/spots/${this.props.match.params.id}/images/${imageId}`,
      method: 'Delete',
      headers: {Authorization: `Bearer ${Auth.getToken()}`},
      json: true
    })
      .then(() => {
        this.getThisSpot()
        this.setState({ sent: 'true', comment: {} })
      })
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  openModal() {
    const options = {
      fromSources: ['local_file_system','instagram','facebook'],
      accept: ['image/*'],
      transformations: {
        crop: true,
        circle: true,
        rotate: true
      },
      onFileUploadFinished: (file) => {
        this.setState({ image: file.url })
      },
      onFileUploadFailed: (file, error) => {
        console.log('file', file)
        console.log('error', error)
      }
    }
    client.picker(options).open()
  }

  updateState(url){
    console.log('updateState running')
    console.log(url)
  }

  render() {
    return(
      <div className="container center-align">
        <div className="row">
          <div className="row valign-wrapper">
            <h2 className="col s8 offset-s2">{this.state.spot.name}</h2>
            <div className="col s3 m2 l2">
              <br />
              {this.state.spot.locationlat && !this.state.spot.liked_by.some(checkLikes) && <a onClick={this.likeButton} className="btn-floating btn-large waves-effect waves-light red accent-3">
                <i className="material-icons">thumb_up</i></a>}
              {this.state.spot.locationlat && this.state.spot.liked_by.some(checkLikes) && <a className="btn-floating btn-large waves-effect waves-light red accent-3">
                <i className="material-icons">check</i></a>}
              {this.state.spot.liked_by && this.state.spot.liked_by.length > 0 && <h6 className="no-top-margin">{this.state.spot.liked_by.length}&nbsp;&nbsp;Likes</h6>}
            </div>
          </div>

          <div className="row">
            <div className="col left-align l6 m12 s12">
              {this.state.spot.locationlat && this.state.points &&
                      <Map
                        center={this.mapCenter}
                        points={this.state.points}
                        locationlat={this.state.spot.locationlat}
                        locationlon={this.state.spot.locationlon}
                      />
              }
            </div>
            {this.state.spot.locationlat &&
            <div className="col left-align l6 m12 s12">
              <Slider>
                {this.state.spot.images.map((image, i) => (
                  <Slide key={i} image={<img src={image.path} />}>{i > 0 && image.creator && this.isImageOwner(image.creator.id) && <div className="caption right-align">
                    <a href="/home" className="btn waves-effect red accent-3" onClick={() => this.deleteImage(image.id)}>Delete Image</a>
                  </div>}</Slide>))}
              </Slider>
            </div>}
          </div>
          <div className="row">
            {this.state.spot.locationlat &&
              <div className="s12 center-align">
                <h6>Spotted by {this.state.spot.creator.username}</h6>
                <br />
                <Modal header="Add Image" ref={el => this.modal = el} trigger={<Button className="white black-text">Add New Image</Button>}>
                  <div className="row">
                    {!this.state.image ?
                      <Container openModal={this.openModal} className="btn waves-effect white black-text" />
                      :
                      <img src={this.state.image}/>
                    }
                  </div>
                  <button onClick={this.handleImageSubmit} className="btn waves-effect red accent-3">Submit</button>
                </Modal>
                <div className="container">
                  <br />
                  <h5>Artists</h5>
                  {this.state.spot.artists.map((artist, i) => (
                    <Modal key={i} header={artist.name} ref={el => this.artistmodal = el} trigger={<span className="pointer"><a>{artist.name}</a> </span>}>
                      <div className="row valign-wrapper">
                        <div className="col s5 m2 l2">
                          <img src={artist.image} alt="" className="circle responsive-img" />
                        </div>
                        <div className="col s7 m10 l10">
                          <span className="black-text">
                            {artist.bio}
                          </span>
                        </div>
                      </div>
                      <h6><strong>More Works</strong></h6><br />
                      <div className="row">
                        {artist.spots.map((spot, i) => (
                          <Link key={i} to={`/spots/${spot.id}`} onClick="OpenCloseModal()">
                            <div className="col s6 m4 l3">
                              <img src={spot.images[0].path} alt="" className="rounded-img" />
                            </div>
                          </Link>
                        ))}
                      </div>
                    </Modal>))}</div>
                <h5>Categories</h5>
                <div>{this.state.spot.categories.map((category, i) => (
                  <span key={i}>{category.name} / </span>))}</div>
              </div>}
          </div>
          {this.state.spot.creator && this.isOwner() && <span><a className="btn waves-effect red accent-3" href={`/spots/${this.state.spot.id}/edit`}>Edit
          </a>&nbsp;&nbsp;&nbsp;&nbsp;</span>}
          {this.state.spot.creator && this.isOwner() && <a className="btn waves-effect red accent-3" onClick={this.handleDelete}>Delete
          </a>}
        </div>
        <div className="container">
          <h5>Comments</h5>
          <br />
          <form onSubmit={this.handleSubmit}>
            <div className="field">
              <div className="control">
                <textarea cols='60' rows='3'
                  name="content"
                  placeholder="Make a Comment"
                  onChange={this.handleChange}
                  value={this.state.comment.content || ''}
                />
              </div>
            </div>
            <br />
            <button className="btn waves-effect red accent-3">Submit</button>
          </form>
          <br />
          {this.state.spot.locationlat &&
                <div>{this.state.spot.comments.slice(0).reverse().map((comment, i) => (
                  <div key={i}><span>&quot;{comment.content}&quot;</span><p><strong>Written by {comment.creator.username}</strong> on {moment(comment.created_at).format('Do MMMM YYYY')} at {moment(comment.created_at).format('hh:mm')}</p><br /></div>))}</div>}
        </div>
        <br />
      </div>
    )
  }
}

export default spotShow

// <div>{this.state.spot.artists.map((artist, i) => (
//   <span key={i}>{artist.name}, </span>))}</div>
// <div>{this.state.spot.categories.map((category, i) => (
//   <span key={i}>{category.name}, </span>))}</div>

// <Slide image={<img src="https://lh5.googleusercontent.com/p/AF1QipMtzak-8tSN965UrRkbbw2ZvPYA_5njAmSCX6vZ=w203-h152-k-no" />}>
//   <Caption>
//     <h3>
// This is our big Tagline!
//     </h3>
//     <h5 className="light grey-text text-lighten-3">
// Here our small slogan.
//     </h5>
//   </Caption>
// </Slide>
// <Slide image={<img />}>
//   <Caption placement="left">
//     <h3>
// Left Aligned Caption
//     </h3>
//     <h5 className="light grey-text text-lighten-3">
// Here our small slogan.
//     </h5>
//   </Caption>
// </Slide>
// <Slide image={<img />}>
//   <Caption placement="right">
//     <h3>
// Right Aligned Caption
//     </h3>
//     <h5 className="light grey-text text-lighten-3">
// Here our small slogan.
//     </h5>
//   </Caption>
// </Slide>
// <Slide image={<img />}>
//   <Caption>
//     <h3>
// This is our big Tagline!
//     </h3>
//     <h5 className="light grey-text text-lighten-3">
// Here our small slogan.
//     </h5>
//   </Caption>
// </Slide>

// <span key={i}>{artist.name} / </span>))}</div>
