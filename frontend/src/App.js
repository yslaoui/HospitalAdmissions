import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import PatientDetail from './components/PatientDetail';
import Admissions from './components/Admissions'
import MedicationForm from './components/MedicationForm'
import PatientForm from './components/PatientForm'
import Patients from './components/Patients'
import AdmissionForm from './components/AdmissionForm';
import LoginForm from './components/LoginForm';


const App = () => {
  return (
<Router>
      <Routes>
        <Route path="/app/" element={<Home/>} />
        <Route path="/app/patients" element={<Patients/>} />
        <Route path="/app/patients/:id" element={<PatientDetail/>} />
        <Route path="/app/addPatient" element={<PatientForm/>} />
        <Route path="/app/admissions" element={<Admissions/>} />
        <Route path="/app/addAdmission" element={<AdmissionForm/>} />
        <Route path="/app/addMedication" element={<MedicationForm/>} />
        <Route path='/app/login' element={<LoginForm/>}></Route>

      </Routes>
    </Router>
  );
};

export default App;
