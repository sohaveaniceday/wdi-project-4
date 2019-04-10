import React from 'react'
import axios from 'axios'
const key = process.env.REACT_APP_OCD_API_KEY
// const rp = require('request-promise')



class Register extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {
        username: '',
        email: '',
        password: '',
        passwordConfirmation: '',
        location: ''
      },
      error: ''
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleSelect = this.handleSelect.bind(this)
  }

  handleChange({ target: { name , value }}) {
    const data = {...this.state.data, [name]: value}
    const error = ''
    this.setState({ data, error })
  }

  handleSubmit(e) {
    e.preventDefault()
    const data = {...this.state.data}
    axios.get(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(data.location)}&key=${key}`)
      .then(ocdResponse => {
        console.log(ocdResponse)
        const { lat, lng } = ocdResponse.data.results[0].geometry
        axios({
          url: 'api/register',
          method: 'POST',
          data: {
            username: data.username,
            email: data.email,
            password: data.password,
            password_confirmation: data.passwordConfirmation,
            locationlat: lat,
            locationlon: lng
          },
          json: true
        })
          .then(() => this.props.history.push('/login'))
          // .catch(() => this.setState({ error: 'Invalid Input'}))
          .catch(() => console.log(data.username, data.email,  data.password, data.passwordConfirmation, lat, lng))
      })
  }


  handleSelect(value) {
    let data = null
    data = {...this.state.data, categories: value.map(({ value }) => value) }
    this.setState({ data })
  }

  render() {
    return (
      <div className="container">
        <form onSubmit={this.handleSubmit}>
          <div className="row">
            <h2 className="title col s6 offset-s3">Register</h2>
            <div className="row">
              <div className="input-field col s6 offset-s3">
                <label htmlFor="username">Username*</label>
                <input
                  className="validate"
                  type="text"
                  name="username"
                  id="username"
                  value={this.state.data.username}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="row">
              <div className="input-field col s6 offset-s3">
                <label htmlFor="email">Email*</label>
                <input
                  className="validate"
                  type="text"
                  name="email"
                  id="email"
                  value={this.state.data.email}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="row">
              <div className="input-field col s6 offset-s3">
                <label htmlFor="password">Password*</label>
                <input
                  className="validate"
                  type="password"
                  name="password"
                  id="password"
                  value={this.state.data.password}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="row">
              <div className="input-field col s6 offset-s3">
                <label htmlFor="passwordConfirmation">Password Confirmation*</label>
                <input
                  className="validate"
                  type="password"
                  name="passwordConfirmation"
                  id="passwordConfirmation"
                  value={this.state.data.passwordConfirmation}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="row">
              <div className="input-field col s6 offset-s3">
                <label htmlFor="location">Location*</label>
                <input
                  className="validate"
                  type="text"
                  name="location"
                  id="location"
                  value={this.state.data.location}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <button className="btn waves-effect waves-light col s6 offset-s3">Register</button>
          </div>
        </form>
      </div>
    )
  }
}

export default Register
