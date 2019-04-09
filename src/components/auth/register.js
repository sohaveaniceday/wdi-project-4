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
    axios.post('api/register', data)
      .then(() => this.props.history.push('/login'))
      .catch(() => this.setState({ error: 'Invalid Input'}))
  }

  handleSelect(value) {
    let data = null
    data = {...this.state.data, categories: value.map(({ value }) => value) }
    this.setState({ data })
  }

  render() {
    console.log(key)
    return (
      <div className="container">
        <form onSubmit={this.handleSubmit}>
          <h2 className="title">Register</h2>
          <div className="row">
            <div className="row">
              <div className="input-field col s12">
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
              <div className="input-field col s12">
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
              <div className="input-field col s12">
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
              <div className="input-field col s12">
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
              <div className="input-field col s12">
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
            <button className="btn waves-effect waves-light">Register</button>
          </div>
        </form>
      </div>
    )
  }
}

export default Register
