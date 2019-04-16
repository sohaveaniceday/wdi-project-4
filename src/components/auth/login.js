import React from 'react'
import axios from 'axios'

import Auth from '../../lib/auth'
// import {Animated} from 'react-animated-css'

class Login extends React.Component {
  constructor() {
    super()

    this.state = {
      data: { email: '', password: '' },
      error: ''
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({ target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    const error = false
    this.setState({ data, error })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post('api/login', this.state.data)
      .then(res => {
        Auth.setToken(res.data.token)
        this.props.history.push('/')
      })
      .catch(() => {
        this.setState({ error: true })
      })
  }

  render() {
    return (
      <div className="container">
        <form onSubmit={this.handleSubmit}>
          <div className="row">
            <h2 className="col s6 offset-s3">Login</h2>
            <div className="row">
              <div className="input-field col s6 offset-s3">
                <label htmlFor="email">Email</label>
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
                <label htmlFor="password">Password</label>
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
            <button className="btn waves-effect red accent-3 col s6 offset-s3">Login</button>
          </div>
          {this.state.error && <h6 className="red-text center-align">*Invalid Input</h6>}
        </form>
      </div>
    )
  }
}

export default Login
