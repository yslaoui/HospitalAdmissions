import loginServices from '../services/loginServices'
import {Form, Button } from 'react-bootstrap'
import { useEffect, useState, React } from 'react'



const LoginForm = (props) => {

  const [medications, setMedications] = useState([])  
  const [newUserName, setnewUserName] = useState('')
  const [newPassword, setNewPassword] = useState('')

  
  const handleSubmit = (event) => {
    event.preventDefault()
    const user = {
        username: newUserName,
        password: newPassword
    }

    loginServices
      .insert(user)
      .then(response => {
        setnewUserName("")
      })

  }

  const changeName = (event) => {
    setnewUserName(event.target.value)
  }

  const changePassword = (event) => {
    setNewPassword(event.target.value)
  }

  
  console.log({props});
  return (
    <div>
        <h1>Login</h1>
        <Form onSubmit={handleSubmit}>
          <Form.Group>
            <Form.Label> Username:  </Form.Label>
            <Form.Control 
              value={newUserName} 
              onChange={changeName}>
            </Form.Control>
          </Form.Group>

          <Form.Group>
            <Form.Label> Password:  </Form.Label>
            <Form.Control 
              value={newPassword} 
              onChange={changePassword}
              type="password"
              >
            </Form.Control>
          </Form.Group>

          <Button variant='primary' type="submit" >Login </Button>
        </Form>
    </div>
  );
}

export default LoginForm
