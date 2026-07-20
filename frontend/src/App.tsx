import { useEffect, useState,  } from 'react'
import { api } from './services/api'

import './App.css'

function App() {
  const [message, setMessage] = useState("Connecting to the backend...");

  useEffect(() => {
    api.get('/health/')
      .then((response) => {
        setMessage(`Backend is healthy: ${JSON.stringify(response.data)}`);
      })
      .catch(() => {
        setMessage(`Error connecting to the backend`);
      });

  }, []);

  //show the message using tailwindcss classes
  return <div className="bg-gray-800 text-white min-h-screen flex items-center justify-center">
    <h1 className="text-4xl">{message}</h1>
  </div>
}
export default App
