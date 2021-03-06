import React from 'react'
import ReactDOM from 'react-dom'
import './style/main.scss'
import { BrowserRouter as Browser, Route, Switch } from 'react-router-dom'

import 'materialize-css'
import 'materialize-css/dist/css/materialize.min.css'

import Nav from './components/common/nav'
import SecureRoute from './components/common/secureRoute'
import Register from './components/auth/register'
import Login from './components/auth/login'
import Landing from './components/landing'
import Home from './components/home'
import SpotShow from './components/spots/spotShow'
import SpotNew from './components/spots/spotNew'
import SpotEdit from './components/spots/spotEdit'
import Search from './components/search/searchResults'
import ErrorPage from './components/errorPage'

const App = () => {

  return (
    <Browser>
      <Nav />
      <Switch>
        <Route path="/register" component={Register} />
        <Route path="/login" component={Login} />
        <SecureRoute path="/spots/new" component={SpotNew} />
        <SecureRoute path="/spots/:id/edit" component={SpotEdit} />
        <SecureRoute path="/spots/:id" component={SpotShow} />
        <SecureRoute path="/search" component={Search} />
        <SecureRoute exact path="/home" component={Home} />
        <Route exact path="/" component={Landing} />
        <Route path="/*" component={ErrorPage} />
      </Switch>
    </Browser>
  )
}


ReactDOM.render(
  <App />,
  document.getElementById('root')
)
