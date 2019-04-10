import React from 'react'
import mapboxgl from 'mapbox-gl'
//the below ensures we're not posting our token onlinw
mapboxgl.accessToken = process.env.MAPBOX_ACCESS_TOKEN

class Map extends React.Component {

  constructor() {
    super()

    this.markers = []
  }

  componentDidMount() {
    this.map = new mapboxgl.Map({
      container: this.mapDiv,
      style: 'mapbox://styles/mapbox/streets-v9',
      center: {lat: this.props.locationlat, lng: this.props.locationlon},
      zoom: 12
    })

    this.setMarkers()
  }

  //calls the setMarkers() function
  componentDidUpdate() {
    this.setMarkers()
  }

  //removes the markers first then returns the new set of markers
  setMarkers() {
    this.markers.forEach(marker => marker.remove())
    this.markers = this.props.points.map(point => {
      const popup = new mapboxgl.Popup({ offset: 25, className: 'popup'})
        .setText(
          `Name: ${point.name}`)
      return new mapboxgl.Marker()
        .setLngLat({  lat: point.locationlat, lng: point.locationlon })
        .addTo(this.map)
        .setPopup(popup)
    })
  }

  render() {
    return(
      <div className="map" ref={el => this.mapDiv = el} />
    )
  }
}

export default Map
