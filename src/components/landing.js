import React, { Component } from 'react'
import { Redirect } from 'react-router'
import Auth from '../lib/auth'
import { Link } from 'react-router-dom'

class Landing extends Component {
  render(){

    if(Auth.getToken()){
      return (<Redirect to="/home" />)
    } else {
      return (
        <div className="landing-page valign-wrapper center-align">
          <div className="row">
            <div className="col s10 l4 m6 offset-l4 offset-m3 offset-s1">
              <div className="card-panel welcome">
                <h5 className="intro-logo">Welcome to Tag</h5>
                <h6>Join a community of other graffiti lovers. From Banksy to Stik, easily find the best street art in your neighbourhood and the rest of London. Plus, don&#39;t forget to share your own spots!</h6>
                <br />
                <a className="waves-effect red accent-3 btn-large" href='/register'>Register</a>
                <br />
                <br />
                <div>
                  <span>Already registered? <Link to="/login">Login here.</Link></span>
                </div>
                <br />
              </div>
            </div>
          </div>
        </div>
      )
    }
  }
}
export default Landing
