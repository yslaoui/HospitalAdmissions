import { useEffect, useState } from 'react'
import services from '../services/patientServices'
import Notification from './Notifications'
import Persons from './Admissions'
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

