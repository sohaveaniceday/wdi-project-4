import React from 'react'
import ReactDOM from 'react-dom'
import './style.scss'
import { BrowserRouter as Browser, Route, Switch } from 'react-router-dom'
import axios from 'axios'


import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'

import Nav from './components/common/nav'
import Register from './components/auth/register'
import Login from './components/auth/login'
import Home from './components/home'

class App extends React.Component {
  componentDidMount() {
    axios.get('/api/spots')
      .then(res => console.log(res.data))
      .catch(err => console.log(err))
  }

  render() {
    return (
      <Browser>
        <Nav />
        <Switch>
          <Route path="/register" component={Register} />
          <Route path="/login" component={Login} />
          <Route exact path="/" component={Home} />
        </Switch>
      </Browser>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
