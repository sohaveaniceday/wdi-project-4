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
        <div className="container">
          <p className="title">
            Munch
          </p>
          <p className="subtitle">
            What are you craving?
          </p>
          <div>
            <span>Already registered? <Link to="/login">Login here.</Link></span>
          </div>
        </div>
      )
    }
  }
}
export default Landing
