# Frontend (frontend)

This folder contains the Vite + React frontend for interacting with the chatbot.

---

# Directory Structure

``` 
.
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
├── postcss.config.js
├── public
│   └── vite.svg
├── README.md
├── src
│   ├── App.css
│   ├── App.jsx
│   ├── components
│   │   ├── ChatInput.jsx
│   │   └── ChatWindow.jsx
│   ├── index.css
│   └── main.jsx
├── tailwind.config.js
└── vite.config.js

```

---

# Quick start


1. Install dependencies:

   npm install

2. Run the development server:

   npm run dev

3. Open the app

   - By default Vite will report a local URL (e.g. `http://localhost:5173`). Open it in your browser to access the chat UI.

---
# Notes
Make sure the backend is running and reachable (check `src/main.jsx` / environment config for the API base URL).

---

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

---

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
