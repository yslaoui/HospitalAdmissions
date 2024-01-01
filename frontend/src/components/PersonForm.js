import services from '../services/patientServices'
import {Form, Button } from 'react-bootstrap'


const PersonForm = (props) => {

  /* A form to add name and number*/
    const changeName = (event) => {
      props.setnewname(event.target.value)
    }
  
    const changeNumber = (event) => {
      props.setnewnumber(event.target.value)
    }
  
  
    const handleSubmit = (event) => {
      event.preventDefault()
      const exists = props.people.some(item => item.name === props.newname)
      const samePhoneNumber = props.people.some(item => item.number === props.newnumber)
      console.log(`exists ${exists}`)
      console.log(`samePhoneNumber ${samePhoneNumber}`)
  
      if (!exists) {
        const newPerson = {
          id: props.people.length + 1,
          name: props.newname, 
          number: props.newnumber
        }
        services
          .insert(newPerson)
          .then(response => {
            props.setnotification(`Added ${response.data.name}`)
            setTimeout(() => props.setnotification(null)  , "5000")
            props.setpersons(props.people.concat(newPerson))
            props.setnewname('')
            props.setnewnumber('')
          })
      }
      else {
        if (!samePhoneNumber) {
          if (window.confirm(`${props.newname} is already in the phonebook, replace the older number with the new one ? `)) {
            const originalPerson = props.people.find(x => x.name == props.newname )
            console.log(`originalNote ${originalPerson.name}`)
            const changedPerson = {...originalPerson, number: props.newnumber}
            console.log(`changedNote ${changedPerson.number}`)
            console.log(`id ${changedPerson.id}`)
            const url = `http://localhost:3001/persons/${originalPerson.id}`
            services
              .update(url, changedPerson)
              .then(response => {
                props.setnotification(`Added ${response.data.name}`)
                setTimeout(() => props.setnotification(null)  , "5000")    
                window.location.reload()
              })
              .catch(error => {
                props.setnotificationtype(false)
                props.setnotification(`The person ${props.newname} was already deleted from server`)
                setTimeout(() => {
                  props.setnotification(null)
                  props.setnotificationtype(true)
                  }  
                  , "5000")
                props.setpersons(props.people.filter(p => p.id != originalPerson.id))
              })
          }  
        }
        else {
          alert(`${props.newname} already exists with phone number ${props.newnumber}!`)
        } 
      }
    }
  
    return (
      <>
        <Form onSubmit={handleSubmit}>
          <Form.Group>
            <Form.Label> Name:  </Form.Label>
            <Form.Control 
              value={props.newname} 
              onChange={changeName}>
            </Form.Control>
          </Form.Group>

          <Form.Group>
            <Form.Label> Name:  </Form.Label>
            <Form.Control 
              value={props.newnumber} 
              onChange={changeNumber}>
            </Form.Control>
          </Form.Group>
          <Button variant='primary' type="submit" >add</Button>
          
        </Form>
      </>
    );
  }
  
  export default PersonForm
  