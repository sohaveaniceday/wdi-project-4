import React from 'react'
import axios from 'axios'
const key = process.env.REACT_APP_OCD_API_KEY
const filestackkey = process.env.FILESTACK_KEY
import * as filestack from 'filestack-js'
const client = filestack.init(filestackkey)

import Auth from '../../lib/auth'
import SpotForm from './spotForm'



class SpotNew extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, error: false }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleSelectArtist = this.handleSelectArtist.bind(this)
    this.handleSelectCategory = this.handleSelectCategory.bind(this)
    this.updateState = this.updateState.bind(this)
    this.openModal = this.openModal.bind(this)
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
          url: '/api/spots',
          method: 'POST',
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
          .then((res) => {
            axios({
              url: `/api/spots/${res.data.id}/images`,
              method: 'POST',
              headers: {Authorization: `Bearer ${Auth.getToken()}`},
              data: {
                path: this.state.image
              },
              json: true
            })
              .then(() => {
                this.props.history.push('/home')
              })
              .catch(() => this.setState({ error: true }))
          })
          .catch(() => this.setState({ error: true }))
      })
      .catch(() => this.setState({ error: true }))
  }

  // handleSelect(value) {
  //   let data = null
  //   data = {...this.state.data, categories: value.map(({ value }) => value) }
  //   this.setState({ data })
  // }

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
    console.log(this.state)

    return (
      <div className="home">
        <div className={this.state.image ? 'container' : 'container full-height'}>
          <div className="container">
            <div className="container">
              <div className="row  no-margin">
                <h3 className="col s12">New Spot</h3>
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
                {this.state.error && <h6 className="red-text center-align">*Invalid Input</h6>}
                <br />
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default SpotNew
