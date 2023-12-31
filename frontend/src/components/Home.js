import { useEffect, useState } from 'react'
import services from '../services/services'
import Notification from './Notifications'
import Persons from './Persons'
import PersonForm from './PersonForm'
import Filter from './Filter'
import NavigationBar from './NavigationBar'


const Home = () => {

  return (
    <div className='container'>
      <NavigationBar/>  
    </div>
    
  )
}

export default Home
