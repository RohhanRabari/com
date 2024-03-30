import React, { useState } from 'react';
import axios from 'axios';
import './CreateUser.css';

function CreateUser() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
  
    const handleSubmit = async (event) => {
      event.preventDefault();
  
      try {
        const response = await axios.post('http://localhost:5000/users', {
          username,
          email,
          password,
        });
  
        console.log(response.data);
      } catch (error) {
        console.error('There was an error!', error);
      }
    };
  
    return (
        <form >
            <div >
                <input type="text" placeholder="Jane Doe" aria-label="Full name"/>
                <button type="button">
                Sign Up
                </button>
                <button type="button">
                Cancel
                </button>
            </div>
        </form>
    );
  }
  
  export default CreateUser;