import React from 'react'

class ErrorPage extends React.Component {
  constructor() {
    super()
  }

  render() {
    return (
      <div className="container">
        <h2>404 Error</h2>
        <h3>Page Not Found</h3>
        <h5>We couldnt found the page that you are looking for.</h5>
      </div>
    )
  }
}

export default ErrorPage
