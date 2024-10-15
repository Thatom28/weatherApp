import React, { useState } from 'react';
import './App.css';

function App() {
  const [city, setCity] = useState('');
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState('');

  const getWeather = async () => {
    setError(''); // Reset any previous error
    try {
      const response = await fetch(`http://127.0.0.1:5000/weather?city=${city}`);
      const data = await response.json();
      if (response.ok) {
        setWeather(data);
      } else {
        setError(data.error);
        setWeather(null);
      }
    } catch (error) {
      setError('Error fetching weather data.');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (city.trim()) {
      getWeather();
    } else {
      setError('Please enter a city name.');
    }
  };

  return (
    <div className="App">
      <h1>Weather App</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter city"
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />
        <button type="submit">Get Weather</button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {weather && (
        <div>
          <h2>Weather in {weather.city}</h2>
          <p>Temperature: {weather.temperature} °C</p>
          <p>Description: {weather.description}</p>
        </div>
      )}
    </div>
  );
}

export default App;
