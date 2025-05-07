// src/components/Navbar.jsx
import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav>
      <ul>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/admin">Admin</Link></li>
        <li><Link to="/orangtua">Orangtua</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;