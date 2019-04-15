import React from 'react'
import axios from 'axios'
const key = process.env.REACT_APP_OCD_API_KEY


import Auth from '../../lib/auth'
import SpotForm from './spotForm'

// import * as filestack from 'filestack-js'
// const client = filestack.init('AYoVZLJZuQ2GNd6qd87SYz')

class SpotEdit extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {}, categories: [] }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleSelectArtist = this.handleSelectArtist.bind(this)
    this.handleSelectCategory = this.handleSelectCategory.bind(this)
    // this.updateState = this.updateState.bind(this)
    // this.openModal = this.openModal.bind(this)
  }

  componentDidMount() {
    axios.get('/api/categories')
      .then(res => {
        return res.data.map(category => ({ value: category.id, label: category.name }))
      })
      .then(categories => this.setState({ categories }))
      .catch(err => console.log(err))
    axios.get('/api/artists')
      .then(res => {
        return res.data.map(artist => ({ value: artist.id, label: artist.name }))
      })
      .then(artists => this.setState({ artists }))
      .catch(err => console.log(err))
    axios.get(`/api/spots/${this.props.match.params.id}`)
      .then(res => this.setState({ data: res.data }))
      .catch(err => console.log(err.message))

  }

  handleChange({ target: { name, value }}) {
    const data = {...this.state.change, [name]: value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()
    // let lat = null
    // let lng = null
    // const data = {...this.state.data}
    // // axios.get(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(data.location)}&key=${key}`)
    // //   .then(ocdResponse => {
    // //     console.log('ocd', ocdResponse)
    // //     const { lat, lng } = ocdResponse.data.results[0].geometry
    //     axios({
    //       url: `/api/spots/${this.props.match.params.id}`,
    //       method: 'PUT',
    //       headers: {Authorization: `Bearer ${Auth.getToken()}`},
    //       data: data,
    //       json: true
    //     })
    //       .then(() => {
    //         axios({
    //           url: `/api/spots/${this.props.match.params.id}/images`,
    //           method: 'POST',
    //           headers: {Authorization: `Bearer ${Auth.getToken()}`},
    //           data: {
    //             path: data.path
    //           },
    //           json: true
    //         })
    //           .then(() => {
    //             this.props.history.push('/home')
    //           })
    //           .catch(err => this.setState({ errors: err.response.data.errors }))
    //       })
    //       .catch(err => {
    //         this.setState({ errors: err.response.data.errors })
    //         axios({
    //           url: `/api/spots/${this.props.match.params.id}/images`,
    //           method: 'POST',
    //           headers: {Authorization: `Bearer ${Auth.getToken()}`},
    //           data: {
    //             path: data.path
    //           },
    //           json: true
    //         })
    //           .then(() => {
    //             this.props.history.push('/spots/${this.props.match.params.id}')
    //           })
    //           .catch(err => this.setState({ errors: err.response.data.errors }))
    //       })
      // })
  }

  handleSelectCategory(value) {
    let data = null
    data = {...this.state.data, categories: value.map(({ value }) => value) }
    this.setState({ data })
  }

  handleSelectArtist(value) {
    let data = null
    data = {...this.state.data, artists: value.map(({ value }) => value) }
    this.setState({ data })
  }
  // openModal() {
  //   const options = {
  //     fromSources: ['local_file_system','instagram','facebook'],
  //     accept: ['image/*'],
  //     transformations: {
  //       crop: true,
  //       circle: true,
  //       rotate: true
  //     },
  //     onFileUploadFinished: (file) => {
  //       this.setState({ image: file.url })
  //     },
  //     onFileUploadFailed: (file, error) => {
  //       console.log('file', file)
  //       console.log('error', error)
  //     }
  //   }
  //   client.picker(options).open()
  // }
  //
  // updateState(url){
  //   console.log('updateState running')
  //   console.log(url)
  // }

  render() {
    console.log('state', this.state)
    return (
      <div className="container">
        <SpotForm
          updateState={this.updateState}
          handleChange={this.handleChange}
          handleSubmit={this.handleSubmit}
          handleSelectArtist={this.handleSelectArtist}
          handleSelectCategory={this.handleSelectCategory}
          data={this.state.data}
          categories={this.state.categories}
          artists={this.state.artists}
          errors={this.state.errors}
          openModal={this.openModal}
          image={this.state.image}
        />
      </div>
    )
  }
}

export default SpotEdit
