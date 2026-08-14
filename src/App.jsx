import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home/Home.jsx"; 
import Dashboard from "./pages/dashboard/Dashboard.jsx"; 
import AuthPage from "./pages/login/login.jsx";
import FinancialOnboarding from "./pages/Financial/Financial.jsx";
import Portfolio from "./pages/Portfolio/Portfolio.jsx";
import MarketsPage from "./pages/Market/market.jsx";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/login" element={<AuthPage />} />
        <Route path="/finances" element={<FinancialOnboarding />} />
        <Route path="/portfolio" element={<Portfolio />} />
       
        {/* Updated path to match Navbar link */}
        <Route path="/markets" element={<MarketsPage />} />
        
        {/* Optional fallback route for singular /market */}
        <Route path="/market" element={<MarketsPage />} />
      </Routes>
    </Router>
  );
}

export default App;