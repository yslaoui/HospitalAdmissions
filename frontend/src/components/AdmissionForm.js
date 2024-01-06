import patientServices from '../services/patientServices'
import medicalConditionServices from '../services/medicalConditionServices'
import medicationServices from '../services/medicationServices'
import doctorServices from '../services/doctorServices'
import hospitalServices from '../services/hospitalServices'
import admissionServices from '../services/admissionServices'

import {Form, Button } from 'react-bootstrap'
import { useEffect, useState, React } from 'react'
import { useLocation, useNavigate } from 'react-router-dom';
import insuranceServices from '../services/insuranceServices'
import admissionTypeServices from '../services/admissionTypeServices'
import testResultServices from '../services/testResultServices'
import Admissions from './Admissions'



const AdmissionForm = (props) => {

    const location = useLocation();
    const navigate = useNavigate();
    const [patientToUpdate, setPatientToUpdate] = useState(location.state?.patientToUpdate || {});

    const [admissions, setAdmissions] = useState([])  


    // Attributes with no foreign relationships
   
    const [newStartDate, setnewStartDate] = useState(patientToUpdate?.age || '')
    const [newEndDate, setnewEndDate] = useState(patientToUpdate?.age || '')
    const [newBilling, setnewBilling] = useState(patientToUpdate?.age || '')
    const [newRoomNumber, setnewRoomNumber] = useState(patientToUpdate?.age || '')

    
    // Attributes with one to many foreign relationships
    const [patients, setPatients] = useState([])  
    const [newPatient, setnewPatient] = useState(patientToUpdate?.name || '')


    const [medicalConditions, setmedicalConditions] = useState([])
    const [newMedicalCondition, setnewMedicalCondition] = useState(patientToUpdate?.gender?.gender || '')

    const [doctors, setdoctors] = useState([])
    const [newdoctors, setnewdoctors] = useState(patientToUpdate?.doctor?.doctor || '')
    
    const [hospitals, sethospitals] = useState([])
    const [newhospitals, setnewhospitals] = useState(patientToUpdate?.doctor?.doctor || '')
    
    const [insurances, setinsurances] = useState([])
    const [newinsurances, setnewinsurances] = useState(patientToUpdate?.doctor?.doctor || '')

    const [admissiontypes, setadmissiontypes] = useState([])
    const [newadmissiontypes, setnewadmissiontypes] = useState(patientToUpdate?.doctor?.doctor || '')

    const [testresults, settestresults] = useState([])
    const [newtestresults, setnewtestresults] = useState(patientToUpdate?.doctor?.doctor || '')


    // Attributes with many to many foreign relationships
    const [medications, setMedications] = useState([])
    const [newMedication, setnewMedication] = useState(patientToUpdate?.medication?.length > 0 ? patientToUpdate.medication[0].medication : '');
    
    const [buttonName, setButtonName] = useState('')

    useEffect(()=> {
        // Populating the state variables that hold the whole records for every model
        patientServices
          .getAll()
          .then(response => {
             setPatients(response.data)
        })

        admissionServices
          .getAll()
          .then(response => {
             setAdmissions(response.data)
        })

        
        medicalConditionServices
          .getAll()
          .then(response => {
            setmedicalConditions(response.data)
        })
        doctorServices
          .getAll()
          .then(response => {
            setdoctors(response.data)
        })
        medicationServices
          .getAll()
          .then(response => {
            setMedications(response.data)
          })     

        hospitalServices
          .getAll()
          .then(response => {
             sethospitals(response.data)
           })     

        insuranceServices
           .getAll()
           .then(response => {
              setinsurances(response.data)
            })     
 
        admissionTypeServices
        .getAll()
        .then(response => {
            setadmissiontypes(response.data)
            })     

        testResultServices
        .getAll()
        .then(response => {
            settestresults(response.data)
            })     

        setButtonName("Add")
         
         // If page is refreshed, the state sent by the update button is forgotten 
         return () => {
          navigate('/addAdmission', {state: {}})
         } 
          }, [navigate])



    const handleSubmit = (event) => {
      event.preventDefault()
      
      // One to many foreign relationships
      const selectedMedicalCondtion = medicalConditions.find(x => x.medical_condition == newMedicalCondition)
      const selecteddoctor = doctors.find(x => x.doctor == newdoctors)
      const selectedhospital = hospitals.find(x => x.hospital == newhospitals)
      const selectedinsurance = insurances.find(x => x.insurance == newinsurances)
      const selectedadmissionType = admissiontypes.find(x => x.admission_type == newadmissiontypes)
      const selectedtestResult = testresults.find(x => x.test_result == newtestresults)
      const selectedpatient = patients.find(x => x.name == newPatient)
      const selectedMedication = medications.find(x => x.medication == newMedication)
      

      // Many to many patient vs. medication foreign relationship

      if (patientToUpdate.id) {

        // Updating an existing patient
        console.log(`Updating.... `)
        const changedPerson = {...patientToUpdate, 
              name: newPatient,
              age: newStartDate,
              gender: selectedMedicalCondtion, 
              doctor: selecteddoctor, 
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

        // Creating a new admission
        console.log(`Creating....`)
        const newAdmission = {
          id: admissions.length + 1,
          date_of_admission: newStartDate,
          room_number: newRoomNumber, 
          billing_amount: newBilling,
          discharge_date: newEndDate,           
          patient: selectedpatient,
          hospital: selectedhospital,
          doctor: selecteddoctor,
          medication: selectedMedication, 
          insurance: selectedinsurance, 
          admission_type: selectedadmissionType,
          test_result: selectedtestResult,
          medical_condition: selectedMedicalCondtion

        }
        console.log(newAdmission)
        admissionServices
          .insert(newAdmission)
          .then(response => {
            setnewStartDate('')
            setnewRoomNumber('')
            setnewBilling('')
            setnewEndDate('')
            setnewPatient('')
            setnewdoctors('')
            setnewinsurances('')
            setnewadmissiontypes('')
            setnewMedicalCondition("")
            setnewdoctors("")
            setnewMedication('')
          })  
  
      }
      

    }
  
    const changeName = (event) => {
      setnewPatient(event.target.value)
    }

    const changeStartDate = (event) => {
        setnewStartDate(event.target.value)
    }

    const changeEndDate = (event) => {
        setnewEndDate(event.target.value)
    }

    const changeBilling = (event) => {
        setnewBilling(event.target.value)
    }

    const changeRoomNumber = (event) => {
        setnewRoomNumber(event.target.value)
    }

    const changeMedicalCondition = (event) => {
        setnewMedicalCondition(event.target.value)
    }

    const changedoctor = (event) => {
      setnewdoctors(event.target.value)
    }

    const changehospital = (event) => {
        setnewhospitals(event.target.value)
    }

    const changeinsurance = (event) => {
        setnewinsurances(event.target.value)
    }

    const changeadmissiontype = (event) => {
        setnewadmissiontypes(event.target.value)
    }

    const changetestresult = (event) => {
        setnewtestresults(event.target.value)
    }

    const changeMedication1 = (event) => {
      setnewMedication(event.target.value)
    }


    return (
      <div>
          <Form onSubmit={handleSubmit}>

           <Form.Group>
              <Form.Label> Patient Name  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newPatient}
                onChange={changeName}>
                   <option value="">{newPatient}</option>
                    {patients.map(patient => (
                        <option key={patient.id} value={patient.name}>{patient.name}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group>


            <Form.Group>
              <Form.Label> Medical condition:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newMedicalCondition}
                onChange={changeMedicalCondition}>
                   <option value="">{newMedicalCondition}</option>
                    {medicalConditions.map(condition => (
                        <option key={condition.id} value={condition.medical_condition}>{condition.medical_condition}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group>

            <Form.Group>
              <Form.Label> Room Number:  </Form.Label>
              <Form.Control 
                value={newRoomNumber} 
                onChange={changeRoomNumber}>
              </Form.Control>
            </Form.Group>

            <Form.Group>
                <Form.Label> Date of admissions </Form.Label>
                <Form.Control 
                    type="date"
                    value={newStartDate}
                    onChange={changeStartDate} 
                    />
            </Form.Group>


            <Form.Group>
                <Form.Label> Discharge Date </Form.Label>
                <Form.Control 
                    type="date"
                    value={newEndDate}
                    onChange={changeEndDate} 
                    />
            </Form.Group>


            <Form.Group>
              <Form.Label> Doctor:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newdoctors}
                onChange={changedoctor}>
                  <option value="">{newdoctors}</option>
                    {doctors.map(type => (
                        <option key={type.id} value={type.doctor}>{type.doctor}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group>


            <Form.Group>
              <Form.Label> Hospital:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newhospitals}
                onChange={changehospital}>
                  <option value="">{newhospitals}</option>
                    {hospitals.map(hospital => (
                        <option key={hospital.id} value={hospital.hospital}>{hospital.hospital}</option>
                    )
                )}
              </Form.Control>
            </Form.Group>

            <Form.Group>
              <Form.Label> Insurance:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newinsurances}
                onChange={changeinsurance}>
                  <option value="">{newinsurances}</option>
                    {insurances.map(insurance => (
                        <option key={insurance.id} value={insurance.insurance}>{insurance.insurance}</option>
                    )
                )}
              </Form.Control>
            </Form.Group>
            

            <Form.Group>
              <Form.Label> Admission type:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newadmissiontypes}
                onChange={changeadmissiontype}>
                  <option value="">{newadmissiontypes}</option>
                    {admissiontypes.map(admission => (
                        <option key={admission.id} value={admission.admission_type}>{admission.admission_type}</option>
                    )
                )}
              </Form.Control>
            </Form.Group>


            <Form.Group>
              <Form.Label> Test Result:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newtestresults}
                onChange={changetestresult}>  
                  <option value="">{newtestresults}</option>
                    {testresults.map(test_result => (
                        <option key={test_result.id} value={test_result.test_result}>{test_result.test_result}</option>
                    )
                )}
              </Form.Control>
            </Form.Group>




            <Form.Group>
              <Form.Label> Medication 1:  </Form.Label>
              <Form.Control 
                as = "select"
                value = {newMedication}
                onChange={changeMedication1}>
                  <option value="">{newMedication}</option>
                    {medications.map(medication => (
                        <option key={medication.id} value={medication.medication}>{medication.medication}</option>
                    )
                    )}
              </Form.Control>
            </Form.Group> 



            <Form.Group>
              <Form.Label> Billing:  </Form.Label>
              <Form.Control 
                value={newBilling} 
                onChange={changeBilling}>
              </Form.Control>
            </Form.Group>




            <Button variant='primary' type="submit" >{buttonName}</Button>
          </Form>
      </div>
    );
  }
  




export default AdmissionForm
