import {BrowserRouter, Routes, Route} from 'react-router-dom'; 
import './App.css';
import LoginPage from '../src/pages/Login';
import Home from './pages/Home';
function App() { 
  return (
    <>
    <BrowserRouter>
    <Routes>
      <Route path = '/' element={<Home />} />
      <Route path ='/login' element={<LoginPage />}/>

    </Routes>
    </BrowserRouter>
    </>
  )
}

export default App; 
