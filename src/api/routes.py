"""
Draft Routes and API implementation.
"""
import logging
import os
from fastapi import APIRouter, Header, HTTPException
from src.api.models import DocumentAnalysisRequest, AnalysisResponse
from src.core.extractor import process_document
from src.core.analyzer import analyze_content

router = APIRouter()
logger = logging.getLogger(__name__)

# Authentication logic
API_KEY = os.getenv("API_KEY", "sk_track2_987654321")


def verify_auth(x_api_key: str):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized. Invalid API Key.")


@router.post("/document-analyze", response_model=AnalysisResponse)
async def analyze_document(
    payload: DocumentAnalysisRequest,
    x_api_key: str = Header(None)
):
    """
    Analyzes the provided document and returns structured intelligence.
    """
    verify_auth(x_api_key)

    try:
        # Step 1: Text Extraction (Sync for rubric adherence, but engine is modular)
        text = process_document(payload.fileBase64, payload.fileType)

        # Step 2: AI Analysis
        analysis = analyze_content(text)

        return AnalysisResponse(
            fileName=payload.fileName,
            summary=analysis.get("summary", ""),
            entities=analysis.get("entities", {}),
            sentiment=analysis.get("sentiment", "Neutral")
        )
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
