import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

class Search extends React.Component {
  constructor() {
    super()
    this.state = { data: {search: ''} }
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange({ target: { name, value } }) {
    const data = {...this.state.data, [name]: value }
    const errors = {...this.state.errors, [name]: null }
    this.setState({ data, errors })
    console.log(this.state.data.search)
  }
  handleSubmit(e) {
    e.preventDefault()
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
  render() {
    const { data } = this.state
    // console.log(search)
    console.log('state', this.state)
    return (
      <div className="container">
        <div className="row">
          <form onSubmit={this.handleSubmit}>
            <div className="input-field col s12">
              <h6 htmlFor="search">Search</h6>
              <input
                id='search'
                className='input'
                name="search"
                placeholder="Search names, artists, categories"
                onChange={this.handleChange}
                value={data.search || ''}
              />
            </div>
            <button className="btn waves-effect waves-light">Search</button>
          </form>
          <div className="row">
            <div className="col">
              {this.state.searchResults && this.state.searchResults.map(searchResult => (
                <Link key={searchResult.id} to={`/spots/${searchResult.id}`}>
                  <div className="col s12 m6 l4">
                    <div className="card hoverable">
                      <div className="card-image">
                        <img src={searchResult.images[0].path} />
                        <span className="card-title">{searchResult.name}</span>
                      </div>
                      <div className="card-content black-text">
                        <p>I am a very simple card. I am good at containing small bits of information.
                        I am convenient because I require little markup to use effectively.</p>
                      </div>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        </div>
      </div>
    )
  }
}
export default Search
