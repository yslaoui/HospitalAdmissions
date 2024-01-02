import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import PatientDetail from './components/PatientDetail';
import Admissions from './components/Admissions'
import MedicationForm from './components/MedicationForm'
import PatientForm from './components/PatientForm'

const App = () => {
  return (
<Router>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/patients/:id" element={<PatientDetail/>} />
        <Route path="/admissions" element={<Admissions/>} />
        <Route path="/addMedication" element={<MedicationForm/>} />
        <Route path="/addPatient" element={<PatientForm/>} />

      </Routes>
    </Router>
  );
};

export default App;
