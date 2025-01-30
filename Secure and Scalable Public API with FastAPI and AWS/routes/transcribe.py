from fastapi import APIRouter, Depends, UploadFile, HTTPException, status,Header
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from aws.secrets import validate_api_key
from db.db import get_db
from models.models import TranscriptionJob
from typing import Annotated

router = APIRouter()

@router.post("/transcribe/")
async def transcribe_audio(
    file: UploadFile,
    api_key: Annotated[str | None, Header()],  # API key is retrieved from the header
    db: Session = Depends(get_db),
    user_id:dict = Depends(validate_api_key)
):
    if not user_id:
        return JSONResponse(content={"message" : "Invalid API Key"},status_code=400)


    # Save Job in DB
    transcription_job = TranscriptionJob(
        user_id=user_id, filename=file.filename, status="processing"
    )
    db.add(transcription_job)
    db.commit()
    db.refresh(transcription_job)

    # Simulate Transcription
    transcription_job.status = "completed"
    transcription_job.result = f"Transcribed text for {file.filename}"
    db.commit()

    return {"job_id": transcription_job.id, "status": transcription_job.status, "result": transcription_job.result}
