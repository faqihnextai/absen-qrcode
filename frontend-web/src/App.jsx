// src/App.jsx
import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import AdminDashboard from './pages/AdminDashboard'
import OrangTuaView from './pages/OrangTuaView'

const App = () => {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/admin" element={<AdminDashboard />} />
      <Route path="/orangtua" element={<OrangTuaView />} />
    </Routes>
  )
}

export default App
