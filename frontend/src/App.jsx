import { useState, useEffect, useRef } from 'react';
import ChatWindow from './components/ChatWindow';
import ChatInput from './components/ChatInput';

function App() {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hello! I’m here to help you with your mental health concerns. How are you feeling today?', sentiment: 'neutral' }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const chatEndRef = useRef(null);

  // Scroll to the bottom of the chat window when new messages are added
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Handle sending a message
  const handleSendMessage = async (text) => {
    if (!text.trim()) return;

    // Add user message to the chat
    const userMessage = { sender: 'user', text, sentiment: 'neutral' };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      // Placeholder API call to your backend
      const response = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      });
      const data = await response.json();

      // Add bot response and sentiment
      const botMessage = {
        sender: 'bot',
        text: data.response || 'I’m here to help. Could you share more?',
        sentiment: data.sentiment || 'neutral',
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: 'Sorry, something went wrong. Please try again.', sentiment: 'none' },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen w-full bg-gray-100 flex flex-col">
      <header className="bg-gradient-to-r from-black to-gray-800 text-white p-4">
        <h1 className="text-2xl font-bold">Mental Health Companion</h1>
      </header>
      <div className="flex-1 flex flex-col">
        <ChatWindow messages={messages} isLoading={isLoading} chatEndRef={chatEndRef} />
        <ChatInput onSend={handleSendMessage} isLoading={isLoading} />
      </div>
    </div>
  );
}

export default App;