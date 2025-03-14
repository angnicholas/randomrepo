import logo from './logo.svg';
import './App.css';
import LoginPage from "./pages/login";
import ProtectedPage from "./pages/protectedpage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const yeet = {
  x : 'yass',
}

// const element = 
// <><h3>yeet.x {yeet.x}</h3>
// <p>poggers</p></>

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="protected" element={<ProtectedPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
