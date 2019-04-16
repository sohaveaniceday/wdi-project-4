import React from 'react'
import axios from 'axios'
import Select from 'react-select'
const key = process.env.REACT_APP_OCD_API_KEY


import Auth from '../../lib/auth'

// import * as filestack from 'filestack-js'
// const client = filestack.init('AYoVZLJZuQ2GNd6qd87SYz')

class SpotEdit extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, error: false, categories: [] }

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
      .then(res => {
        axios.get(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(res.data.locationlat)}+${encodeURIComponent(res.data.locationlon)}&key=${key}`)
          .then(ocdResponse => {
            console.log('ocd', ocdResponse)
            const location = ocdResponse.data.results[0].formatted
            const data = {data: { name: res.data.name, location: location, categories: res.data.categories.map(({ id }) => id), artists: res.data.artists.map(({ id }) => id), artistValues: res.data.artists.map(artist => ({ value: artist.id, label: artist.name })), categoryValues: res.data.categories.map(category => ({ value: category.id, label: category.name }))}}
            this.setState(data)
          })
          .catch(err => console.log(err.message))
      })
  }

  handleChange({ target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    const error = false
    this.setState({ data, error })
  }

  handleSubmit(e) {
    e.preventDefault()
    const data = {...this.state.data}
    axios.get(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(data.location)}&key=${key}`)
      .then(ocdResponse => {
        console.log('ocd', ocdResponse)
        const { lat, lng } = ocdResponse.data.results[0].geometry
        axios({
          url: `/api/spots/${this.props.match.params.id}`,
          method: 'PUT',
          headers: {Authorization: `Bearer ${Auth.getToken()}`},
          data: {
            name: data.name,
            locationlat: lat,
            locationlon: lng,
            category_id: data.categories,
            artist_id: data.artists
          },
          json: true
        })
          .then(() => {
            this.props.history.push(`/spots/${this.props.match.params.id}`)
          })
          .catch(() => this.setState({ error: true }))
      })
      .catch(() => this.setState({ error: true }))
  }

  handleSelectCategory(value) {
    let data = null
    data = {...this.state.data, categories: value.map(({ value }) => value), categoryValues: value.map(category => ({ value: category.value, label: category.label }))  }
    this.setState({ data })
  }

  handleSelectArtist(value) {
    let data = null
    data = {...this.state.data, artists: value.map(({ value }) => value), artistValues: value.map(artist => ({ value: artist.value, label: artist.label })) }
    this.setState({ data })
    console.log('val', value)
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
        <div className="container">
          <div className="container">
            <h2>Edit Spot</h2>
            <form onSubmit={this.handleSubmit}>
              <div className="row">
                <div className="input-field col s12">
                  <input
                    className="validate"
                    type="text"
                    name="name"
                    id="name"
                    onChange={this.handleChange}
                    value={this.state.data.name || ' '}
                  />
                  <label className="active" htmlFor="name">Spot Name*</label>
                </div>
              </div>
              <div className="row">
                <div className="input-field col s12">
                  <label htmlFor="location" className="active">Postcode*</label>
                  <input
                    className="validate"
                    type="text"
                    name="location"
                    id="location"
                    onChange={this.handleChange}
                    value={this.state.data.location || ' '}
                  />
                </div>
              </div>
              <div className="row">
                <div className="col s12">
                  <h6 htmlFor="artists">Select Artist(s)*</h6>
                  <div>
                    <Select
                      value={this.state.data.artistValues}
                      id="artists"
                      options={this.state.artists}
                      onChange={this.handleSelectArtist}
                      isMulti
                      className="basic-multi-select"
                      classNamePrefix="select"
                    />
                  </div>
                </div>
              </div>

              <div className="row">
                <div className="field input-field col s12">
                  <h6 htmlFor="categories">Select Categorie(s)*</h6>
                  <div>
                    <Select
                      value={this.state.data.categoryValues}
                      id="categories"
                      options={this.state.categories}
                      onChange={this.handleSelectCategory}
                      isMulti
                      className="basic-multi-select"
                      classNamePrefix="select"
                    />
                  </div>
                </div>
              </div>
              <div className="center-align">
                <button className="btn waves-effect red accent-3 center-align">Submit</button>
              </div>
              {this.state.error && <h6 className="red-text center-align">*Invalid Input</h6>}
            </form>
          </div>
        </div>
      </div>
    )
  }
}

export default SpotEdit
