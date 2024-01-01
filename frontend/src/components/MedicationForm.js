import admissionServices from '../services/admissionServices'
import {Form, Button } from 'react-bootstrap'
import { useEffect, useState, React } from 'react'



const MedicationForm = (props) => {

  const [newName, setnewName] = useState('')

  const handleSubmit = () => {}
  
  const changeName = (event) => {
    setnewName(event.target.value)
  }

  console.log({props});
  return (
    <div>
        <Form onSubmit={handleSubmit}>
          <Form.Group>
            <Form.Label> Name:  </Form.Label>
            <Form.Control 
              value={newName} 
              onChange={changeName}>
            </Form.Control>
          </Form.Group>
        </Form>
    </div>
  );
}

export default MedicationForm
