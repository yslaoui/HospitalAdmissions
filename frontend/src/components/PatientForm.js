import patientServices from '../services/patientServices'
import genderServices from '../services/genderServices'
import bloodTypeServices from '../services/bloodTypeServices'

import {Form, Button } from 'react-bootstrap'
import { useEffect, useState, React } from 'react'
import medicationServices from '../services/medicationServices'


const PatientForm = (props) => {
    const [patients, setPatients] = useState([])  
    const [newName, setnewName] = useState('')

    const [newAge, setnewAge] = useState('')
    
    const [genders, setGenders] = useState([])
    const [newGender, setnewGender] = useState('Male')
    const [selectedGender, setSelectedGender] = useState({})

    const [blood_types, setBlood_types] = useState([])
    const [newBlood_type, setNewBlood_type] = useState('')
    const [selectedBloodType, setselectedBloodType] = useState({})
    


    const [medications, setMedications] = useState([])
    const [newMedication, setNewMedication] = useState('Aspegic')
  
    useEffect(()=> {
        // Populating the state variables that hold the whole records for every model
        patientServices
          .getAll()
          .then(response => {
             setPatients(response.data)
        })
        genderServices
          .getAll()
          .then(response => {
            setGenders(response.data)
        })
        bloodTypeServices
          .getAll()
          .then(response => {
            setBlood_types(response.data)
        })
        medicationServices
          .getAll()
          .then(response => {
            setMedications(response.data)
          })      
     }, [])

    
    const handleSubmit = (event) => {
      event.preventDefault()
      const newPatient = {
        id: patients.length + 1,
        name: newName, 
        age: newAge, 
        gender: selectedGender, 
        blood_type: selectedBloodType, 
        medication: newMedication 
      }
      patientServices
        .insert(newPatient)
        .then(response => {
          console.log(response.data)
          console.log(newPatient)
          setnewName('')
          setnewAge('')
          setNewMedication('')
          setBlood_types([])

        })
  
    }
  
    const changeName = (event) => {
      setnewName(event.target.value)
    }

    const changeAge = (event) => {
        setnewAge(event.target.value)
    }

    const changeGender = (event) => {
        setSelectedGender(genders.find(x => x.gender == event.target.value ))
        setnewGender(event.target.value)
    }

    const changeBlood_type = (event) => {
      setselectedBloodType(blood_types.find(x => x.blood_type == event.target.value ))
      setNewBlood_type(event.target.value)
    }

    const changeMedication = (event) => {
      setNewMedication(event.target.value)
    }


    return (
      <div>
          <Form onSubmit={handleSubmit}>
            <Form.Group>
              <Form.Label> Patient:  </Form.Label>
              <Form.Control 
                value={newName} 
                onChange={changeName}>
              </Form.Control>
            </Form.Group>

            <Form.Group>
              <Form.Label> Age:  </Form.Label>
              <Form.Control 
                value={newAge} 
                onChange={changeAge}>
              </Form.Control>
            </Form.Group>

            <Form.Group>
              <Form.Label> Gender:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newGender}
                onChange={changeGender}>
                    {genders.map(gender => (
                        <option key={gender.id} value={gender.gender}>{gender.gender}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group>


            <Form.Group>
              <Form.Label> Blood Type:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newBlood_type}
                onChange={changeBlood_type}>
                    {blood_types.map(type => (
                        <option key={type.id} value={type.blood_type}>{type.blood_type}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group>



            <Form.Group>
              <Form.Label> Medication:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newMedication}
                onChange={changeMedication}>
                    {medications.map(medication => (
                        <option key={medication.id} value={medication.medication}>{medication.medication}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group>


            <Button variant='primary' type="submit" >add</Button>
          </Form>
      </div>
    );
  }
  




export default PatientForm
