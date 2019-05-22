import React from 'react'
import axios from 'axios'

const key = process.env.REACT_APP_OCD_API_KEY

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
      error: false
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleSelect = this.handleSelect.bind(this)
  }

  handleChange({ target: { name , value }}) {
    const data = {...this.state.data, [name]: value}
    const error = false
    this.setState({ data, error })
  }

  handleSubmit(e) {
    e.preventDefault()
    const data = {...this.state.data}
    axios.get(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(data.location)}&key=${key}`)
      .then(ocdResponse => {
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
          .catch(() => {
            console.log('error')
            this.setState( {error: true} )
          })
      })
      .catch(() => {
        console.log('error')
        this.setState( {error: true} )
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
            <h2 className="col s6 offset-s3">Register</h2>
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
                <label htmlFor="location">Postcode*</label>
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
            <button className="btn waves-effect red accent-3 col s6 offset-s3">Register</button>
          </div>
          {this.state.error && <h6 className="red-text center-align">*Invalid Input</h6>}
        </form>
      </div>
    )
  }
}

export default Register
