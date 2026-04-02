"""
API Data Models.
"""
from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class DocumentRequest(BaseModel):
    fileName: str = Field(..., description="Uploaded file name")
    fileType: str = Field(..., description="One of: 'pdf', 'docx', 'image'")
    fileBase64: str = Field(..., description="Base64 encoded string of the file.")


class EntityExtraction(BaseModel):
    names: List[str] = []
    dates: List[str] = []
    organizations: List[str] = []
    amounts: List[str] = []


class DocumentResponse(BaseModel):
    status: str = "success"
    fileName: str
    summary: str
    entities: EntityExtraction
    sentiment: str
