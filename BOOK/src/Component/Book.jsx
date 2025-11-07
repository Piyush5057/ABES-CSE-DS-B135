import React from 'react'
import './Book.css'



function Book(props) {
  return (
    <div id='Book'>
        <img src="https://th.bing.com/th/id/OIP.aNm1aoymx1IjRc3_3nuGowHaL3?w=197&h=316&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3" alt="" height={100} width={100}/>
        <h1>Title:{props.name}</h1>
        <h1>Price:{props.price}</h1>
    </div>
  )
}

export default Book