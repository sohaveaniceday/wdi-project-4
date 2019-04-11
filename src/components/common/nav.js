import React from 'react'
import { Link, withRouter } from 'react-router-dom'

import Auth from '../../lib/auth'



class Nav extends React.Component {
  constructor() {
    super()


    this.logout = this.logout.bind(this)
  }

  logout() {
    Auth.logout()
    this.props.history.push('/')
  }




  render() {
    return (
      <div>
        <nav>
          <div className="nav-wrapper">
            {!Auth.isAuthenticated() && <Link className="brand-logo" to="/login">Logo</Link>}
            {Auth.isAuthenticated() && <Link className="brand-logo" to="/home">Logo</Link>}
            <a href="#" data-target="mobile-demo" className="sidenav-trigger"><i className="material-icons">menu</i></a>
            <ul className="right hide-on-med-and-down">
              {Auth.isAuthenticated() && <li><Link to="/spots/new">New Spot</Link></li>}
              {Auth.isAuthenticated() && <li><a onClick={this.logout}>Logout</a></li>}
              {!Auth.isAuthenticated() && <li><Link to="/register">Register</Link></li>}
              {!Auth.isAuthenticated() && <li><Link to="/login">Login</Link></li>}
            </ul>
          </div>
        </nav>

        <ul className="sidenav" id="mobile-demo">
          {Auth.isAuthenticated() && <li><a onClick={this.logout}>Logout</a></li>}
          {!Auth.isAuthenticated() && <li><Link to="/register">Register</Link></li>}
          {!Auth.isAuthenticated() && <li><Link to="/login">Login</Link></li>}
        </ul>
      </div>
    )
  }
}

export default withRouter(Nav)
