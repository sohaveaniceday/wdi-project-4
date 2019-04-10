import React from 'react'
import axios from 'axios'
import Auth from '../lib/auth'
import Map from './common/map'


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
      <div className="container">
        {this.state.data.username && <h2>Hello {this.state.data.username}</h2>}
        <form onSubmit={this.handleSubmit}>
          <div className="input-field">
            <input id="search" type="search" required />
            <label className="label-icon" htmlFor="search"><i className="material-icons">search</i></label>
            <i className="material-icons">close</i>
            <button className="btn waves-effect waves-light">Search</button>
          </div>
        </form>
        <div>
          <h2>Graffiti Spots Near You</h2>
          {this.state.points &&
            <Map
              center={this.mapCenter}
              points={this.state.points}
              locationlat={this.state.data.locationlat}
              locationlon={this.state.data.locationlon}
            />
          }
        </div>
        <div className="row">
        </div>
        <div className="row">
        </div>
        <div className="row">
        </div>
      </div>
    )
  }
}

export default Home
