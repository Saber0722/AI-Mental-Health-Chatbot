# Backend (backend)

This folder contains the Node.js backend that exposes the chatbot API and integrates with the model inference utilities.

---
# Directory Structure

``` 
.
├── package.json
├── package-lock.json
├── README.md
└── server.js

```
---
# Quick start


1. Install dependencies:

   npm install

2. Configure:

   - Ensure model artifacts are available and that any config values (API ports, model paths) are set in environment variables or config files used by the server.

3. Run the server (development):

   npm start

---
# Notes
- The backend expects model artifacts or a way to call inference code from `ai_model/`. Confirm paths and permissions before starting.
