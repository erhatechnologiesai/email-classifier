from pydantic import BaseModel
from typing import List

class EmailPayload(BaseModel):
    subject: str
    body: str

class EmailClassification(BaseModel):
    category: str # PROMOTIONAL, TRANSACTIONAL, SUPPORT, SECURITY, SPAM
    confidence: float
    target_folder: str
