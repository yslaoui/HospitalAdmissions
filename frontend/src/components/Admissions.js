import admissionServices from '../services/admissionServices'
import Table from 'react-bootstrap/Table';
import { Link, redirectDocument } from 'react-router-dom';
import { useEffect, useState } from 'react'
import {Form, Button } from 'react-bootstrap'




const Admissions = (props) => {
    /*Returns a list of filtered persons each with a delete button*/ 
    const [admissions, setAdmissions] = useState([])
    useEffect(()=> {
      admissionServices
        .getAll()
        .then(response => {
          setAdmissions(response.data)
        })
     }, [])

     const handleDelete = (id) => {
      console.log(`Deleting ${id}`)
      const resourceURL = ` http://127.0.0.1:8080/api/admissions/${id}`
      const resourceToDelete = admissions.find(x => x.id==id)
      console.log(resourceURL)
      console.log(resourceToDelete)
      if (window.confirm( `Delete admission number ${resourceToDelete.id} for patient ${resourceToDelete.patient.name} ? `))
        admissionServices
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
  
  
    return (
      <div>
        <h1> Table of admissions</h1>
        <Table striped>
          <tbody>
            <tr>
              <th> Action</th>
              <th> Patient name</th>
              <th> medical Condition</th>
              <th> Date of admission</th>
              <th> Doctor</th>
              <th> Hospital</th>
              <th> Insurance Provider</th>
              <th> Billing Amount</th>
              <th> Admission type</th>
              <th> Discharge date</th>
              <th> Medication</th>
              <th> Test results</th>
            </tr>
            {admissions.map((elem, index) => {
              return(
                <tr key={elem.id}>
                  <td> 
                    <Button variant='primary' type="submit" >Update</Button> 
                    <Button variant='danger' type="submit"onClick={()=>handleDelete(elem.id)} >Delete</Button> 
                    
                    </td>

                  <td> 
                    <Link to={`/patients/${elem.patient.id}`}> {elem.patient.name}   </Link>    
                  </td>
                  <td> {elem.medical_condition.medical_condition}</td>
                  <td> {elem.date_of_admission}</td>
                  <td> {elem.doctor.doctor} </td>
                  <td> {elem.hospital.hospital} </td>
                  <td> {elem.insurance.insurance} </td>
                  <td> {elem.billing_amount} </td>
                  <td> {elem.admission_type.admission_type} </td>
                  <td> {elem.discharge_date} </td>
                  <td> {elem.medication.medication} </td>
                  <td> {elem.test_result.test_result} </td>
              </tr>
              )
            })}
          </tbody>

        </Table>
      </div>
    );
  }

  export default Admissions
  

