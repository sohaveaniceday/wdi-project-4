import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import m from 'materialize-css'
import Auth from '../../lib/auth'

class Nav extends React.Component {
  constructor() {
    super()

    this.logout = this.logout.bind(this)
  }

  componentDidMount() {
    m.Sidenav.init(this.sidenav)
  }

  logout() {
    Auth.logout()
    this.props.history.push('/')
  }

  render() {
    return (
      <div>
        <div className="navbar-fixed">
          <nav className="red accent-3">
            <div className="nav-wrapper">
              {!Auth.isAuthenticated() && (
                <Link className="brand-logo main-logo" to="/">
                  &nbsp;&nbsp;Tag
                </Link>
              )}
              {Auth.isAuthenticated() && (
                <Link className="brand-logo main-logo" to="/home">
                  &nbsp;&nbsp;Tag
                </Link>
              )}
              <a
                href="#"
                data-target="mobile-demo"
                className="sidenav-trigger right"
              >
                <i className="material-icons">menu</i>
              </a>
              <ul className="right hide-on-med-and-down">
                {Auth.isAuthenticated() && (
                  <li>
                    <Link to="/search">Search</Link>
                  </li>
                )}
                {Auth.isAuthenticated() && (
                  <li>
                    <Link to="/spots/new">New Spot</Link>
                  </li>
                )}
                {Auth.isAuthenticated() && (
                  <li>
                    <a onClick={this.logout}>
                    Logout
                    </a>
                  </li>
                )}
                {!Auth.isAuthenticated() && (
                  <li>
                    <Link to="/register">Register</Link>
                  </li>
                )}
                {!Auth.isAuthenticated() && (
                  <li>
                    <Link to="/login">Login</Link>
                  </li>
                )}
              </ul>
            </div>
          </nav>
        </div>

        <ul
          className="sidenav right"
          ref={el => (this.sidenav = el)}
          id="mobile-demo"
        >
          {Auth.isAuthenticated() && (
            <li>
              <Link to="/search">Search</Link>
            </li>
          )}
          {Auth.isAuthenticated() && (
            <li>
              <Link to="/spots/new">New Spot</Link>
            </li>
          )}
          {Auth.isAuthenticated() && (
            <li>
              <a onClick={this.logout}>
              Logout
              </a>
            </li>
          )}
          {!Auth.isAuthenticated() && (
            <li>
              <Link to="/register">Register</Link>
            </li>
          )}
          {!Auth.isAuthenticated() && (
            <li>
              <Link to="/login">Login</Link>
            </li>
          )}
        </ul>
      </div>
    )
  }
}

export default withRouter(Nav)
