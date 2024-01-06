import patientServices from '../services/patientServices'
import Table from 'react-bootstrap/Table';
import { Link, redirectDocument } from 'react-router-dom';
import { useEffect, useState } from 'react'
import {Form, Button } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom';




const Patients = (props) => {
    /*Returns a list of filtered persons each with a delete button*/ 
    const navigate = useNavigate();
    const [patients, setPatients] = useState([])
    useEffect(()=> {
      patientServices
        .getAll()
        .then(response => {
          setPatients(response.data)
        })
     }, [])

     const handleDelete = (id) => {
      console.log(`Deleting ${id}`)
      const resourceURL = ` http://127.0.0.1:8080/api/patients/${id}`
      const resourceToDelete = patients.find(x => x.id==id)
      console.log(resourceURL)
      console.log(resourceToDelete)
      if (window.confirm( `Delete patient number ${resourceToDelete.id} for patient ${resourceToDelete.name} ? `))
        patientServices
         .destroy(resourceURL)
         .then(response => {
            window.location.reload()
            console.log(` successfully deleted resource ${response}`)
         }) 
         .catch(error => {
          console.log(`error deleting resource ${error}`)
         })
      
        console.log(`great`)
    } 


    const handleUpdate = (id) => {
        const patientToUpdate = patients.find(x => x.id == id )
        navigate('/addPatient', { state: { patientToUpdate } });
    }
  
  
    return (
      <div>
        <h1> Table of patients</h1>
        <Table striped>
          <tbody>
            <tr>
              <th> Action</th>
              <th> Name</th>
              <th> Age</th>
              <th> Gender</th>
              <th> Blood Type</th>
            </tr>
            {patients.map((elem, index) => {
              return(
                <tr key={elem.id}>
                  <td> 
                    <Button variant='primary' type="submit" onClick = {()=>handleUpdate(elem.id)} >Update</Button> 
                    <Button variant='danger' type="submit" onClick={()=>handleDelete(elem.id)} >Delete</Button> 
                    </td>

                  <td> 
                    <Link to={`/patients/${elem.id}`}> {elem.name} </Link>    
                  </td>
                  <td> {elem.age}</td>
                  <td> {elem.gender?.gender || 'Unknown'}</td> 
                  <td> {elem.blood_type?.blood_type || 'Unknown'}</td> 
                  {/* <td> {elem.gender.gender}</td>
                  <td> {elem.blood_type.gender} </td> */}
              </tr>
              )
            })}
          </tbody>

        </Table>
      </div>
    );
  }

  export default Patients
  

