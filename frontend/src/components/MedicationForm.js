import medicationServices from '../services/medicationServices'
import {Form, Button } from 'react-bootstrap'
import { useEffect, useState, React } from 'react'



const MedicationForm = (props) => {

  const [medications, setMedications] = useState([])  
  const [newName, setnewName] = useState('')

  useEffect(()=> {
    medicationServices
      .getAll()
      .then(response => {
        setMedications(response.data)
      })
   }, [])
  
  const handleSubmit = (event) => {
    event.preventDefault()
    const newMedication = {
      id: medications.length + 1,
      medication: newName
    }
    medicationServices
      .insert(newMedication)
      .then(response => {
        setnewName("")
      })

  }

  const changeName = (event) => {
    setnewName(event.target.value)
  }
  
  console.log({props});
  return (
    <div>
        <Form onSubmit={handleSubmit}>
          <Form.Group>
            <Form.Label> Medication:  </Form.Label>
            <Form.Control 
              value={newName} 
              onChange={changeName}>
            </Form.Control>
          </Form.Group>
          <Button variant='primary' type="submit" >add</Button>
        </Form>
    </div>
  );
}

export default MedicationForm
