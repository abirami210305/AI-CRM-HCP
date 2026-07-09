from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from config import GROQ_API_KEY
from ai.agent import run_agent
import models
from database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print(GROQ_API_KEY)
@app.get("/")
def home():
    return {"message": "AI CRM Backend Running"}

@app.post("/log-interaction")
def log_interaction(data: dict):

    db: Session = SessionLocal()

    interaction = models.Interaction(
        doctor=data["doctor"],
        hospital=data["hospital"],
        date=data["date"],
        type=data["type"],
        notes=data["notes"]
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    db.close()

    return {
        "status": "Success",
        "message": "Interaction Logged Successfully",
        "id": interaction.id
    }


@app.post("/chat")
def chat(data: dict):

    reply = run_agent(data["message"])

    return {
        "reply": reply
    }