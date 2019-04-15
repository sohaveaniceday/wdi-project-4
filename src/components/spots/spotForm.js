import React from 'react'
import Select from 'react-select'
import Container from '../common/container'

const SpotForm = ({ handleChange, handleSubmit, handleSelectArtist, handleSelectCategory, data, artists, categories, image, openModal }) => {
  return (
    <form onSubmit={handleSubmit}>
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
          <label htmlFor="location">Postcode*</label>
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
      {// <div className="row">
      //   <div className="input-field col s12">
      //     <label htmlFor="path">Image*</label>
      //     <input
      //       className="validate"
      //       type="text"
      //       name="path"
      //       id="path"
      //       onChange={handleChange}
      //       value={data.path || ''}
      //     />
      //   </div>
      // </div>
      }

      <div className="row">
        <div className="field">
          {!image ?
            <Container openModal={openModal} className="btn waves-effect red accent-3" />
            :
            <img src={image}/>
          }
        </div>
      </div>


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
      <div className="center-align">
        <button className="btn waves-effect red accent-3 center-align">Submit</button>
      </div>
    </form>
  )
}

export default SpotForm
