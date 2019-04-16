import React from 'react'
import axios from 'axios'
import Auth from '../lib/auth'
import Map from './common/map'
import { Link } from 'react-router-dom'



class Home extends React.Component {
  constructor() {
    super()

    this.state = { data: {}, errors: {} }
    //below is read only! Can't reassign in anything outside of state. If you need to update something, add it to state. Create this to stop you repeating yourself.
    this.mapCenter = { lat: 51.515, lng: -0.078 }

    // this.handleClick = this.handleClick.bind(this)

  }

  // the const is 'deconstructing' the object, basically shortening taking 2 keys into 1 line.
  //the 'this.getBikePoints(lat, lng, 1000)' parses the data from this.mapCenter and '1000' into the getBikePoints function
  componentDidMount() {
    axios.get(`/api/users/${Auth.getPayload().sub}`)
      .then(res => this.setState({ data: res.data }))
    const { lat, lng } = this.mapCenter
    this.getSpots(lat, lng, 8000)
  }

  //this grabs from the TFL api. Params specifies the bits of information we need. The .then function takes the responses (res) and maps the places to a new state - points!
  getSpots(locationlat, locationlon, radius) {
    axios.get('/api/spots', {
      params: { locationlat, locationlon, radius }
    })
      .then(res => {
        console.log('res', res)
        this.setState({ points: res.data })
      })
  }


  render() {
    console.log('state', this.state)
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

// {this.state.data.username && <h2>Hello {this.state.data.username}!</h2>}
