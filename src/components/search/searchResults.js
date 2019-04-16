import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

class Search extends React.Component {
  constructor() {
    super()
    this.state = { data: {search: ''} }
    // this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  componentDidMount() {
    axios.all([
      axios.get('/api/spots')
    ])
      .then(res => {
        const searchResults = res[0].data
        this.setState({ searchResults })
      })
  }

  handleChange({ target: { name, value } }) {
    const data = {...this.state.data, [name]: value }
    const errors = {...this.state.errors, [name]: null }
    this.setState({ data, errors })
    console.log(this.state.data.search)
    this.setState({ sent: true })
    axios.all([
      axios.get('/api/spots')
    ])
      .then(res => {
        const searchItem = this.state.data.search.toLowerCase()
        console.log('res', res)
        const searchResults = res[0].data.filter(result => {
          return (result.name.toLowerCase().includes(searchItem) || result.categories.some(category => {
            return category.name.toLowerCase().includes(searchItem)
          }) || result.artists.some(artist => {
            return artist.name.toLowerCase().includes(searchItem)
          })
          )
        })
        this.setState({ searchResults })
      })
  }
  // handleSubmit(e) {
  //   e.preventDefault()
  //   this.setState({ sent: true })
  //   axios.all([
  //     axios.get('/api/spots')
  //   ])
  //     .then(res => {
  //       const searchItem = this.state.data.search.toLowerCase()
  //       console.log('res', res)
  //       const searchResults = res[0].data.filter(result => {
  //         return (result.name.toLowerCase().includes(searchItem) || result.categories.some(category => {
  //           return category.name.toLowerCase().includes(searchItem)
  //         }) || result.artists.some(artist => {
  //           return artist.name.toLowerCase().includes(searchItem)
  //         })
  //         )
  //       })
  //       this.setState({ searchResults })
  //     })
  // }
  render() {
    const { data } = this.state
    // console.log(search)
    console.log('state', this.state)
    return (
      <div className={this.state.searchResults && this.state.searchResults.length < 4 ? 'home full-height' : 'home'}>
        <div className={this.state.searchResults ? 'container' : 'container full-height'}>
          <div className="row no-margin">
            <div className="input-field col s12 center-align">
              <h5 htmlFor="search">Search</h5>
              <input
                id='search'
                className='input'
                name="search"
                placeholder="Search names, artists, categories"
                onChange={this.handleChange}
                value={data.search || ''}
              />
            </div>
            <div className="row">
              <div className="col">
                {this.state.searchResults && this.state.searchResults.slice(0).reverse().map(searchResult => (
                  <Link key={searchResult.id} to={`/spots/${searchResult.id}`}>
                    <div className="col s12 m6 l4">
                      <div className="card hoverable">
                        <div className="card-image">
                          <img src={searchResult.images[0].path} />
                          <span className="card-title">{searchResult.name}</span>
                        </div>
                        <div className="card-content black-text">
                          <div className="row valign-wrapper">
                            <div className="col s8">{searchResult.artists.map((artist, i) => (
                              <h6 key={i}>By {artist.name}</h6>))}
                            </div>
                            <div className="col s3">
                              <span>{searchResult.liked_by.length > 0 ? <p>{searchResult.liked_by.length}&nbsp;&nbsp;<i className="material-icons tiny">thumb_up</i></p> : <p>0&nbsp;&nbsp;<i className="material-icons tiny">thumb_up</i></p>}</span>
                            </div>
                          </div>
                          <div className="row">
                            <div className="col s12"><p><strong>&nbsp;&nbsp;&nbsp;&nbsp;Categories:</strong><br />
                              <span>&nbsp;&nbsp;&nbsp;&nbsp;{searchResult.categories.map((category, i) => (
                                <span key={i}>{category.name} / </span>))}
                              </span>
                            </p>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </Link>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
export default Search
