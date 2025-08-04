import React, { useState } from 'react';

function App() {
  const [apiResponse, setApiResponse] = useState('...');

  const testDb = async () => {
    setApiResponse('Loading...');
    try {
      const response = await fetch('/api/test_db');
      const data = await response.json();
      setApiResponse(JSON.stringify(data));
    } catch (error: any) {
      setApiResponse('Error: ' + error.message);
    }
  };

  return (
    <div>
      <h1>Walking Skeleton Test</h1>
      <p>Click the button to test the backend API and its database connection.</p>
      <button onClick={testDb}>Test Database</button>
      <p>API Response: <b>{apiResponse}</b></p>
    </div>
  );
}

export default App;
