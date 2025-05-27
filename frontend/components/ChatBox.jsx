import React, { useState } from 'react';
import axios from 'axios';

const ChatBox = () => {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (!query.trim()) return;

    const userMessage = { sender: 'user', text: query };
    setMessages((prev) => [...prev, userMessage]);
    setQuery('');

    try {
      const response = await axios.post(
        `${import.meta.env.VITE_BACKEND_URL}/ask`,
        { question: query }
      );
      const botMessage = { sender: 'bot', text: response.data.answer };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      const errorMessage = {
        sender: 'bot',
        text: 'Sorry, something went wrong. Please try again.',
      };
      setMessages((prev) => [...prev, errorMessage]);
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '1rem' }}>
      <h2>Chat with your Documents</h2>
      <div
        style={{
          border: '1px solid #ccc',
          borderRadius: '8px',
          padding: '1rem',
          height: '400px',
          overflowY: 'auto',
          backgroundColor: '#f9f9f9',
        }}
      >
        {messages.map((msg, idx) => (
          <div
            key={idx}
            style={{
              textAlign: msg.sender === 'user' ? 'right' : 'left',
              margin: '0.5rem 0',
            }}
          >
            <span
              style={{
                display: 'inline-block',
                padding: '0.5rem 1rem',
                borderRadius: '16px',
                backgroundColor:
                  msg.sender === 'user' ? '#007bff' : '#e0e0e0',
                color: msg.sender === 'user' ? '#fff' : '#000',
                maxWidth: '75%',
              }}
            >
              {msg.text}
            </span>
          </div>
        ))}
      </div>
      <div style={{ marginTop: '1rem', display: 'flex' }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Type your question..."
          style={{
            flex: 1,
            padding: '0.5rem',
            fontSize: '1rem',
            borderRadius: '4px',
            border: '1px solid #ccc',
          }}
        />
        <button
          onClick={handleSend}
          style={{
            marginLeft: '0.5rem',
            padding: '0.5rem 1rem',
            backgroundColor: '#007bff',
            color: '#fff',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBox;
