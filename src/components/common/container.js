import React from 'react'


const Container = (props) => {
  return(
    <button
      className={props.className}
      onClick={props.openModal}
      type="button"
    >
      Upload Image
    </button>
  )
}
export default Container
