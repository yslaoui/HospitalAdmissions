import patientServices from '../services/patientServices'
import genderServices from '../services/genderServices'
import bloodTypeServices from '../services/bloodTypeServices'

import {Form, Button } from 'react-bootstrap'
import { useEffect, useState, React } from 'react'
import medicationServices from '../services/medicationServices'
import { useLocation, useNavigate } from 'react-router-dom';



const PatientForm = (props) => {

    const location = useLocation();
    const navigate = useNavigate();
    const [patientToUpdate, setPatientToUpdate] = useState(location.state?.patientToUpdate || {});

    const [patients, setPatients] = useState([])  
   
    // Attributes with no foreign relationships
    const [newName, setnewName] = useState(patientToUpdate?.name || '')
    const [newAge, setnewAge] = useState(patientToUpdate?.age || '')
    
    // Attributes with one to many foreign relationships
    const [genders, setGenders] = useState([])
    const [newGender, setnewGender] = useState(patientToUpdate?.gender?.gender || '')

    const [blood_types, setBlood_types] = useState([])
    const [newBlood_type, setNewBlood_type] = useState(patientToUpdate?.blood_type?.blood_type || '')
    
    // Attributes with many to many foreign relationships
    const [medications, setMedications] = useState([])
    const [newMedication1, setNewMedication1] = useState(patientToUpdate?.medication?.length > 0 ? patientToUpdate.medication[0].medication : '');
    const [newMedication2, setNewMedication2] = useState(patientToUpdate?.medication?.length > 1 ? patientToUpdate.medication[0].medication : '');
    
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
         
         // If page is refreshed, the state sent by the update button is forgotten 
         return () => {
          navigate('/addPatient', {state: {}})
         } 
     }, [navigate])

    const handleSubmit = (event) => {
      event.preventDefault()
      
      // One to many foreign relationships
      const selectedGender = genders.find(x => x.gender == newGender)
      const selectedBloodType = blood_types.find(x => x.blood_type == newBlood_type)
      
      // Many to many patient vs. medication foreign relationship
      const medication1 = medications.find(x => x.medication == newMedication1)
      const medication2 = medications.find(x => x.medication == newMedication2)
      const manySelectedMedications = [].concat(medication1, medication2)  

      if (patientToUpdate.id) {
        console.log(`Updating.... `)
        const changedPerson = {...patientToUpdate, 
              name: newName,
              age: newAge,
              gender: selectedGender, 
              blood_type: selectedBloodType, 
              medication: manySelectedMedications     
            }
        console.log(changedPerson)
        const url = `http://127.0.0.1:8080/api/patients/${patientToUpdate.id}`
        patientServices
        .update(url, changedPerson)
        .then(response => {    
          console.log(`Gut`)
        })
        .catch(error => {
          console.log(error)
        })

      }
      else {
        // Creating a new patient
        console.log(`Creating....`)
        const newPatient = {
          id: patients.length + 1,
          name: newName, 
          age: newAge, 
          gender: selectedGender, 
          blood_type: selectedBloodType, 
          medication: manySelectedMedications 
        }
        console.log(newPatient)
        patientServices
          .insert(newPatient)
          .then(response => {
            setnewName('')
            setnewAge('')
            setnewGender("")
            setNewBlood_type("")
            setNewMedication1('')
            setNewMedication2('')
          })  
  
      }
      

    }
  
    const changeName = (event) => {
      setnewName(event.target.value)
    }

    const changeAge = (event) => {
        setnewAge(event.target.value)
    }

    const changeGender = (event) => {
        setnewGender(event.target.value)
    }

    const changeBlood_type = (event) => {
      setNewBlood_type(event.target.value)
    }

    const changeMedication1 = (event) => {
      setNewMedication1(event.target.value)
    }

    const changeMedication2 = (event) => {
      setNewMedication2(event.target.value)
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
                   <option value="">{newGender}</option>
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
                  <option value="">{newBlood_type}</option>
                    {blood_types.map(type => (
                        <option key={type.id} value={type.blood_type}>{type.blood_type}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group>


            <Form.Group>
              <Form.Label> Medication 1:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newMedication1}
                onChange={changeMedication1}>
                  <option value="">{newMedication1}</option>
                    {medications.map(medication => (
                        <option key={medication.id} value={medication.medication}>{medication.medication}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group> 

            <Form.Group>
              <Form.Label> Medication 2:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newMedication2}
                onChange={changeMedication2}>
                  <option value="">{newMedication2}</option>
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
