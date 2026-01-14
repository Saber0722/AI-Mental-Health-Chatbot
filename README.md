# AI Mental Health Chatbot

This repository contains an end-to-end prototype of an AI-powered mental health chatbot. It includes components for training and running conversational AI models, a backend server that exposes the bot via an API, and a web frontend to interact with the bot.
This project is intended for research and prototyping only — it is not a substitute for professional mental health care.

---

# Directory Structure

``` 
.
├── ai_model
│   ├── dialogue_generation
│   ├── load_dialogue_generation.py
│   ├── load_sentimental_analysis.py
│   ├── README.md
│   ├── requirements.txt
│   └── sentiment_analysis
├── backend
│   ├── package.json
│   ├── package-lock.json
│   ├── README.md
│   └── server.js
├── frontend
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── postcss.config.js
│   ├── public
│   ├── README.md
│   ├── src
│   ├── tailwind.config.js
│   └── vite.config.js
└── README.md

```
Note:
- [`ai_model/`](ai_model/README.md) — Training and inference code, datasets, and model artifacts. See the AI Training README: `ai_model/README.md`.
- [`backend/`](backend/README.md) — Node.js backend that serves the chatbot API and integrates the model. See backend README: `backend/README.md`.
- [`frontend/`](frontend/README.md) — Vite + React frontend for the chat UI. See frontend README: `frontend/README.md`.
- Other files: project-level configuration and auxiliary scripts.

---

# How to run

## Follow these steps in order:

1. AI Model Training

   - Before running the backend, you must have trained or downloaded model artifacts placed under `ai_model/models/`.
   - See [`ai_model/README.md`](ai_model/README.md) for step-by-step training and inference instructions, dependencies, and tips for using the provided models.

2. Backend

   - The backend reads model artifacts (or calls the inference utilities) and exposes HTTP endpoints the frontend uses.
   - See [`backend/README.md`](backend/README.md) for installation and run commands (node/npm based).

3. Frontend

   - The frontend runs a Vite development server and connects to the backend API to exchange chat messages.
   - See [`frontend/README.md`](frontend/README.md)  for installation and run commands (npm/yarn).

---
# Ethical concerns and disclaimer

- Not a professional: This chatbot is a research/prototype system and should not be used as a replacement for professional mental health care.
- Accuracy & safety: The model may produce incorrect, biased, or inappropriate responses. It is not guaranteed to be factually accurate or safe.
- No emergency use: Do not rely on this system for crisis or emergency situations. Always call local emergency services or a crisis hotline when needed.
- Data privacy: Be mindful of any PII or sensitive user data used during training or inference. Remove or anonymize sensitive data before storing or sharing.

If you plan to deploy this publicly or use it with real users, consult appropriate clinical, legal, and security experts and implement guardrails (content filters, human-in-the-loop, logging and monitoring, etc.).

---
# Additional information

- Contributing: Please open issues or pull requests for bugs and improvements.
- License: Check the repository license (if present) or add one before public distribution.

Thank you for exploring this project. See the component READMEs below to continue.


