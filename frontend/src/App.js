import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import PatientDetail from './components/PatientDetail';
import Admissions from './components/Admissions'
import MedicationForm from './components/MedicationForm'
import PatientForm from './components/PatientForm'
import Patients from './components/Patients'
import AdmissionForm from './components/AdmissionForm';



const App = () => {
  return (
<Router>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/patients" element={<Patients/>} />
        <Route path="/patients/:id" element={<PatientDetail/>} />
        <Route path="/addPatient" element={<PatientForm/>} />
        <Route path="/admissions" element={<Admissions/>} />
        <Route path="/addAdmission" element={<AdmissionForm/>} />
        <Route path="/addMedication" element={<MedicationForm/>} />

      </Routes>
    </Router>
  );
};

export default App;
