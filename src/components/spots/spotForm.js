import React from 'react'
import Select from 'react-select'
// import Container from '../Container'

const SpotForm = ({ handleChange, handleSubmit, handleSelectArtist, handleSelectCategory, data, artists, categories }) => {
  return (
    <div className="container">
      <form onSubmit={handleSubmit}>
        <div className="row">
          <h1 className="title col s12">Spot Form</h1>
          <div className="row">
            <div className="input-field col s12">
              <label htmlFor="name">Spot Name*</label>
              <input
                className="validate"
                type="text"
                name="name"
                id="name"
                onChange={handleChange}
                value={data.name || ''}
              />
            </div>
          </div>
          <div className="row">
            <div className="input-field col s12">
              <label htmlFor="location">Location*</label>
              <input
                className="validate"
                type="text"
                name="location"
                id="location"
                onChange={handleChange}
                value={data.location || ''}
              />
            </div>
          </div>
          <div className="row">
            <div className="input-field col s12">
              <label htmlFor="path">Image*</label>
              <input
                className="validate"
                type="text"
                name="path"
                id="path"
                onChange={handleChange}
                value={data.path || ''}
              />
            </div>
          </div>

          {
            // <div className="field">
          //   <label className="label">Review Image</label>
          //   {!image ?
          //     <Container openModal={openModal} className="button is-warning is-rounded" />
          //     :
          //     <img src={image}/>
          //   }
          // </div>
          /*<div className="field">
          <label className="label">Review Image</label>
          {!this.props.image ?
            <Container openModal={this.openModal} className="button is-info is-rounded" />
            :
            <img src={this.props.image}/>
          }

        </div>*/}


          <div className="row">
            <div className="col s12">
              <h6 htmlFor="artists">Select Artists*</h6>
              <div>
                <Select
                  id="artists"
                  options={artists}
                  onChange={handleSelectArtist}
                  isMulti
                  className="basic-multi-select"
                  classNamePrefix="select"
                />
              </div>
            </div>
          </div>

          <div className="row">
            <div className="field input-field col s12">
              <h6 htmlFor="categories">Select Categories*</h6>
              <div>
                <Select
                  id="categories"
                  options={categories}
                  onChange={handleSelectCategory}
                  isMulti
                  className="basic-multi-select"
                  classNamePrefix="select"
                />
              </div>
            </div>
          </div>
          <button className="btn waves-effect waves-light">Submit</button>
        </div>
      </form>
    </div>
  )
}

export default SpotForm
