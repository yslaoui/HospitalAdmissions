import { Navbar, Nav, Container } from 'react-bootstrap';
import { useEffect, useState, React } from 'react'
import patientServices from '../services/patientServices'
import admissionServices from '../services/admissionServices'
import {Form, Button } from 'react-bootstrap'
import Admissions from './Admissions';


const Summary = () => {

    const [patientCount, setPatientCount] = useState(0)
    const [admissionCount, setAdmissionCount] = useState(0)

    useEffect(()=> {
        patientServices
          .getAll()
          .then(response => {
            setPatientCount(response.data.length)
          })
        admissionServices
          .getAll()
          .then(response => {
            setAdmissionCount(response.data.length)
          })

       }, [])



  return (
    <div>
        <p> {patientCount} patients <Button variant='primary' type="submit" href="/addPatient" > Add a patient </Button>  </p>
        <p> {admissionCount} admissions <Button variant='primary' type="submit" href="/addPatient" > Add an admission </Button> </p>
        <Admissions title = "Latest admissions"/>
    </div>
  );
};

export default Summary;
