import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [answer, setAnswer] = useState('');

  const handleAsk = async () => {
    const res = await axios.post(`${import.meta.env.VITE_BACKEND_URL}/ask`, {
      question: query
    });
    setAnswer(res.data.answer);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>OpenShift RAG Assistant</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question..."
        style={{ width: '60%', padding: '0.5rem', fontSize: '1rem' }}
      />
      <button onClick={handleAsk} style={{ marginLeft: '1rem' }}>
        Ask
      </button>
      <div style={{ marginTop: '2rem', fontSize: '1.1rem' }}>
        <strong>Answer:</strong>
        <p>{answer}</p>
      </div>
    </div>
  );
}

export default App;
