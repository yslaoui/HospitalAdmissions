import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import PersonDetail from './components/PersonDetail';

const App = () => {
  return (
<Router>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/persons/:id" element={<PersonDetail/>} />
      </Routes>
    </Router>
  );
};

export default App;
