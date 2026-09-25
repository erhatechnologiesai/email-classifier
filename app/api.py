from fastapi import FastAPI
from app.config import settings
from app.models import EmailPayload, EmailClassification
from app.services.classifier_service import classify_email_content

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/classify-email", response_model=EmailClassification)
def classify_email(payload: EmailPayload):
    cat, conf, folder = classify_email_content(payload.subject, payload.body)
    return EmailClassification(category=cat, confidence=conf, target_folder=folder)
