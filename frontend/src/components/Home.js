import { useEffect, useState } from 'react'
import services from '../services/patientServices'
import Notification from './Notifications'
import Persons from './Admissions'
import PersonForm from './PersonForm'
import Filter from './Filter'
import NavigationBar from './NavigationBar'
import Summary  from './Summary'


const Home = () => {

  return (
    <div className='container'>
      <NavigationBar/> 
      <Summary/> 
    </div>
    
  )
}

export default Home

