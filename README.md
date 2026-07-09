# AI CRM for Healthcare Professionals

## Overview

AI CRM for Healthcare Professionals is a Full Stack AI-powered CRM application that helps medical representatives manage doctor interactions efficiently. The application uses AI to log interactions, search records, summarize conversations, edit interactions, and create follow-up reminders.

---

## Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- FastAPI
- Python

### Database
- SQLite

### AI
- LangGraph 1.2.8
- Groq Llama 3.3 70B Versatile

---

## Features

- Log HCP interactions
- AI Chat Assistant
- Search previous interactions
- Edit interaction details
- Summarize interactions
- Follow-up reminders
- SQLite database storage

---

## Project Structure

```
AI-CRM-HCP
│
├── backend
│
├── frontend
│
└── README.md
```

---

## Installation

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## API Endpoints

POST /log-interaction

POST /chat

GET /

---

## Author

Abirami Elangovan