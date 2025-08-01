import React, { useState, useRef, useEffect } from 'react';
import './App.css';

interface Message {
  id: number;
  sender: 'user' | 'ai';
  text: string;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(scrollToBottom, [messages]);

  const handleSendMessage = async () => {
    if (input.trim()) {
      const newUserMessage: Message = {
        id: messages.length + 1,
        sender: 'user',
        text: input.trim(),
      };
      setMessages((prevMessages) => [...prevMessages, newUserMessage]);
      setInput('');

      const aiThinkingMessage: Message = {
        id: messages.length + 2,
        sender: 'ai',
        text: 'Thinking...',
      };
      setMessages((prevMessages) => [...prevMessages, aiThinkingMessage]);

      try {
        const response = await fetch('http://34.47.243.114:8000/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: newUserMessage.text }),
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.detail || 'Something went wrong');
        }

        const data = await response.json();
        const aiActualResponseText = data.response;

        setMessages((prevMessages) =>
          prevMessages.map((msg) =>
            msg.id === aiThinkingMessage.id ? { ...msg, text: aiActualResponseText } : msg
          )
        );
      } catch (error) {
        console.error('Error sending message to backend:', error);
        setMessages((prevMessages) =>
          prevMessages.map((msg) =>
            msg.id === aiThinkingMessage.id ? { ...msg, text: `Error: ${error instanceof Error ? error.message : String(error)}` } : msg
          )
        );
      }
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cabinet Secretary Portal</h1>
      </header>
      <div className="chat-container">
        <div className="messages-display">
          {messages.map((message) => (
            <div key={message.id} className={`message ${message.sender}`}>
              <div className="message-bubble">{message.text}</div>
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>
        <div className="input-area">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message..."
            className="message-input"
          />
          <button onClick={handleSendMessage} className="send-button">
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
