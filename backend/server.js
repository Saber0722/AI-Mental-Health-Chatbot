const express = require('express');
const { PythonShell } = require('python-shell');
const cors = require('cors');
const path = require('path');

const app = express();
const port = 5000;

// Middleware
app.use(cors());
app.use(express.json());

// API endpoint for chat
app.post('/api/chat', async (req, res) => {
  const { message } = req.body;

  if (!message || typeof message !== 'string') {
    return res.status(400).json({ error: 'Invalid message' });
  }

  try {
    // Sentiment analysis
    const sentimentResult = await new Promise((resolve, reject) => {
      PythonShell.run('load_sentimental_analysis.py', {
        mode: 'text',
        pythonPath: '/mnt/d/GitHub/AI_Mental_Health_ChatBot/ai_model/ai_venv/bin/python3',
        scriptPath: path.join(__dirname, '../ai_model'),
        args: [message],
      }, (err, results) => {
        if (err) {
          console.error('Sentiment Error:', err);
          return reject(err);
        }
        resolve(results ? results[0] : 'neutral');
      });
    });

    // Dialogue generation
    const dialogueResult = await new Promise((resolve, reject) => {
      PythonShell.run('load_dialogue_generation.py', {
        mode: 'text',
        pythonPath: '/mnt/d/GitHub/AI_Mental_Health_ChatBot/ai_model/ai_venv/bin/python3',
        scriptPath: path.join(__dirname, '../ai_model'),
        args: [message],
      }, (err, results) => {
        if (err) {
          console.error('Dialogue Error:', err);
          return reject(err);
        }
        resolve(results ? results[0] : 'I’m here to help. Could you share more?');
      });
    });

    // Send response
    res.json({
      response: dialogueResult,
      sentiment: sentimentResult,
    });

  } catch (error) {
    console.error('Server Error:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
