import React from 'react'
import axios from 'axios'
import Map from '../common/map'
const moment = require('moment')
// import M from 'materialize-css'
import { Slider, Slide, Modal, Button } from 'react-materialize'
import Auth from '../../lib/auth'


class spotShow extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {}, user: {}, spot: {}, comment: {} }

    this.handleDelete = this.handleDelete.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleImageSubmit = this.handleImageSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
    this.mapCenter = { lat: 51.515, lng: -0.078 }
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
    this.getSpots(lat, lng, 8000)
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

  handleChange({ target: { name, value } }) {
    const comment = {...this.state.comment, [name]: value }
    const errors = {...this.state.errors, [name]: null }
    this.setState({ comment, errors })
    console.log(this.state)
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

  handleImageSubmit() {
    axios({
      url: `/api/spots/${this.props.match.params.id}/images`,
      method: 'POST',
      headers: {Authorization: `Bearer ${Auth.getToken()}`},
      data: {
        path: this.state.comment.path
      },
      json: true
    })
      .then(() => {
        this.getThisSpot()
        this.setState({ sent: 'true', comment: {} })
        document.location.reload(true)
        // const instance = M.Modal.getInstance(this.modal)
        // console.log(instance)
        // instance.close()
      })
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  render() {
    console.log('state', this.state)
    return(
      <div className="container center-align">
        <div className="row">
          <h2 className="col s12">{this.state.spot.name}</h2>
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
                  <Slide key={i} image={<img src={image.path} />}></Slide>))}
              </Slider>
            </div>}
            <div className="row">
              {this.state.spot.locationlat &&
              <div className="s12 center-align">
                <h6>Created by {this.state.spot.creator.username}</h6>
                <Modal header="Add Image" ref={el => this.modal = el} trigger={<Button>Add New Image</Button>}>
                  <input
                    className="validate"
                    type="text"
                    name="path"
                    id="path"
                    onChange={this.handleChange}
                    value={this.state.comment.path || ''}
                  />
                  <button onClick={this.handleImageSubmit} className="btn waves-effect waves-light">Submit</button>
                </Modal>
                <h5>Artists</h5>
                <div>{this.state.spot.artists.map((artist, i) => (
                  <Modal key={i} header={artist.name} ref={el => this.artistmodal = el} trigger={<span><a>{artist.name}</a> / </span>}>
                    <div className="row valign-wrapper">
                      <div className="col s2">
                        <img src={artist.image} alt="" className="circle responsive-img" />
                      </div>
                      <div className="col s10">
                        <span className="black-text">
                          {artist.bio}
                        </span>
                      </div>
                    </div>
                  </Modal>))}</div>
                <h5>Categories</h5>
                <div>{this.state.spot.categories.map((category, i) => (
                  <span key={i}>{category.name} / </span>))}</div>
              </div>}
            </div>
            {this.state.spot.creator && this.isOwner() && <a className="btn waves-effect waves-light" href={`/spots/${this.state.spot.id}/edit`}>Edit
            </a>}
            {this.state.spot.creator && this.isOwner() && <a className="btn waves-effect waves-light" onClick={this.handleDelete}>Delete
            </a>}
          </div>
          <h4 className="title is-4">Comments</h4>
          <form onSubmit={this.handleSubmit}>
            <div className="field">
              <label className="label">Make Comment</label>
              <div className="control">
                <textarea cols='60' rows='3'
                  name="content"
                  placeholder="Comment"
                  onChange={this.handleChange}
                  value={this.state.comment.content || ''}
                />
              </div>
            </div>
            <button className="btn waves-effect waves-light">Submit</button>
          </form>
          <br />
          {this.state.spot.locationlat &&
              <div>{this.state.spot.comments.map((comment, i) => (
                <div key={i}><span>&quot;{comment.content}&quot;</span><p><strong>Written by {comment.creator.username}</strong> on {moment(comment.created_at).format('Do MMMM YYYY')} at {moment(comment.created_at).format('hh:mm')}</p><br /></div>))}</div>}
        </div>
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
