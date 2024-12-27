import {  Routes, Route } from "react-router";
import {
  PasswordInput,
  PasswordStrengthMeter,
} from "@/components/ui/password-input"
import { useState } from 'react'
import './App.css'
import Home from "@/pages/Home"
import About from "@/pages/About"
import Login from "@/pages/Login"
import Register from "@/pages/Register"
import AuthLayout from "./layouts/Authlayout";

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Routes>
        <Route index element={<Home />} />
        <Route path="about" element={<About />} />

        {/* <Route element={<AuthLayout />}> */}
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
        {/* </Route> */}

        {/* <Route path="concerts">
          <Route index element={<ConcertsHome />} />
          <Route path=":city" element={<City />} />
          <Route path="trending" element={<Trending />} />
        </Route> */}
      </Routes>

    </>
  )
}

export default App
