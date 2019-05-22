import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Auth from '../lib/auth'
import Map from './common/map'

class Home extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {} }
    this.mapCenter = { lat: 51.515, lng: -0.078 }
  }

  componentDidMount() {
    axios.get(`/api/users/${Auth.getPayload().sub}`)
      .then(res => this.setState({ data: res.data }))
    const { lat, lng } = this.mapCenter
    this.getSpots(lat, lng, 8000)
  }

  getSpots(locationlat, locationlon, radius) {
    axios.get('/api/spots', {
      params: { locationlat, locationlon, radius }
    })
      .then(res => {
        this.setState({ points: res.data })
      })
  }

  render() {
    return(
      <div className="home">
        <div className="container full-height">
          <div className="row">
            {this.state.points &&
            <><h3 className="center-align col s12">Street Art Near You</h3>
            <div className="row">
              <br />
              <Map
                center={this.mapCenter}
                points={this.state.points}
                locationlat={this.state.data.locationlat}
                locationlon={this.state.data.locationlon}
              />
            </div></>}
          </div>
          <div className="row">
            <Link to="/search" className="center-align col l4 offset-l4 m6 offset-m3 s12 btn waves-effect red accent-3">Search</Link>
          </div>
          <div className="row">
            <Link to="/spots/new" className="center-align col l4 offset-l4 m6 offset-m3 s12 btn waves-effect red accent-3">New Spot</Link>
          </div>
        </div>
      </div>
    )
  }
}

export default Home