import admissionServices from '../services/admissionServices'
import Table from 'react-bootstrap/Table';
import { Link, redirectDocument } from 'react-router-dom';
import { useEffect, useState } from 'react'




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
  
  
    return (
      <div>
        <h1> Table of admissions</h1>
        <Table striped>
          <tbody>
            <tr>
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
                  <tD> {elem.test_result.test_result} </tD>
              </tr>
              )
            })}
          </tbody>

        </Table>
      </div>
    );
  }

  export default Admissions
  

