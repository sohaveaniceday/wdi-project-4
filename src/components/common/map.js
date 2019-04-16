import 'mapbox-gl/dist/mapbox-gl.css'
import React from 'react'
import mapboxgl from 'mapbox-gl'
import MapboxGeocoder from 'mapbox-gl-geocoder'
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
    this.map.addControl(new MapboxGeocoder({
      accessToken: mapboxgl.accessToken,
      mapboxgl: mapboxgl
    }))

    this.setMarkers()
  }

  //calls the setMarkers() function
  // componentDidUpdate() {
  //   this.setMarkers()
  // }

  //removes the markers first then returns the new set of markers
  setMarkers() {
    this.markers.forEach(marker => marker.remove())
    this.markers = this.props.points.map(point => {
      const popup = new mapboxgl.Popup({ offset: 25, className: 'popup'})
        .setHTML(
          `<a href="/spots/${point.id}">
          <div class="center-align">
          <div class="center-align">
            <span>
              <p>&nbsp;&nbsp;${point.name}</p>
            </span>
          </div>
              <div class="center-align">
          <img src=${point.images[0].path} alt="" class="rounded-img" />
          </div>
          </div>
            </a>`)
      new mapboxgl.Marker()
        .setLngLat({  lat: point.locationlat, lng: point.locationlon })
        .addTo(this.map)
        .setPopup(popup)
      // return new mapboxgl.Marker()
      //   .setLngLat({  lat: this.props.locationlat, lng: this.props.locationlon })
      //   .addTo(this.map)
    })
    var el = document.createElement('div')
    el.className = 'center-marker'
    new mapboxgl.Marker(el)
      .setLngLat({  lat: this.props.locationlat, lng: this.props.locationlon })
      .addTo(this.map)
  }

  render() {
    return(
      <div className="map" ref={el => this.mapDiv = el} />
    )
  }
}

export default Map
