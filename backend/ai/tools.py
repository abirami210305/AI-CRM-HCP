from langchain.tools import tool
from sqlalchemy.orm import Session

import models
from database import SessionLocal


print("log_interaction tool executed")
@tool
def log_interaction(
    doctor: str,
    hospital: str,
    notes: str
):
    """Log a doctor interaction into the CRM database."""

    print("log_interaction tool executed")

    db: Session = SessionLocal()

    interaction = models.Interaction(
        doctor=doctor,
        hospital=hospital,
        date="2026-07-09",
        type="Chat",
        notes=notes
    )

    db.add(interaction)
    db.commit()
    db.close()

    return {
    "status": "success",
    "message": f"Interaction saved for {doctor}"
}

@tool
def edit_interaction(
    doctor: str,
    new_notes: str
):
    """Edit interaction notes using doctor name."""

    db: Session = SessionLocal()

    interaction = db.query(models.Interaction).filter(
        models.Interaction.doctor == doctor
    ).first()

    if interaction is None:
        db.close()
        return "Interaction not found."

    interaction.notes = new_notes

    db.commit()
    db.close()

    return f"Interaction updated for {doctor}."

@tool
def search_interaction(keyword: str):
    """Search interactions by doctor or hospital."""

    db: Session = SessionLocal()

    results = db.query(models.Interaction).filter(
        (models.Interaction.doctor.contains(keyword)) |
        (models.Interaction.hospital.contains(keyword))
    ).all()

    db.close()

    if not results:
        return "No interactions found."

    response = ""

    for item in results:
        response += (
            f"Doctor: {item.doctor}\n"
            f"Hospital: {item.hospital}\n"
            f"Notes: {item.notes}\n\n"
        )

    return response

@tool
def summarize_interaction():
    """Summarize all interactions."""

    db: Session = SessionLocal()

    interactions = db.query(models.Interaction).all()

    db.close()

    if not interactions:
        return "No interactions found."

    summary = ""

    for item in interactions:
        summary += (
            f"Doctor: {item.doctor}, "
            f"Hospital: {item.hospital}, "
            f"Notes: {item.notes}\n"
        )

    return summary

@tool
def followup_reminder(
    doctor: str,
    reminder_date: str
):
    """Create a follow-up reminder."""

    return (
        f"Follow-up reminder created.\n"
        f"Doctor: {doctor}\n"
        f"Date: {reminder_date}"
    )