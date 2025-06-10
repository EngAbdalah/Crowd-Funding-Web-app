// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ReportsList from './pages/ReportsList';
import ReportDetails from './pages/ReportDetails';
import { CssBaseline, Container } from '@mui/material';

function App() {
  return (
    <Router>
      <CssBaseline />
      <Container maxWidth="lg">
        <Routes>
          <Route path="/reports" element={<ReportsList />} />
          <Route path="/reports/:id" element={<ReportDetails />} />
          <Route path="/" element={<ReportsList />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;