"""
Draft Routes and API implementation.
"""
import logging
import os
from fastapi import APIRouter, Header, HTTPException, BackgroundTasks
from src.api.models import DocumentRequest, DocumentResponse
from src.core.extractor import process_document
from src.core.analyzer import analyze_content
import logging
import time
import uuid

router = APIRouter()
logger = logging.getLogger(__name__)

# In-memory store for task results (simulating a DB for the hackathon UI)
# Note: In a real prod environment, use Redis/PostgreSQL.
processing_results = {}

def background_processing_task(task_id: str, file_name: str, file_type: str, file_base64: str):
    """Background task to process extraction and AI analysis."""
    try:
        # 1. Extraction
        start_time = time.time()
        text = process_document(file_base64, file_type)
        extract_time = time.time() - start_time
        
        # 2. AI Analysis
        analysis = analyze_content(text)
        
        # 3. Store result
        processing_results[task_id] = {
            "status": "success",
            "fileName": file_name,
            "summary": analysis.get("summary", "N/A"),
            "entities": analysis.get("entities", {}),
            "sentiment": analysis.get("sentiment", "Neutral"),
            "metrics": {
                "extract_time": round(extract_time, 2),
                "total_time": round(time.time() - start_time, 2)
            }
        }
        logger.info(f"Task {task_id} completed successfully.")
    except Exception as e:
        logger.error(f"Task {task_id} failed: {str(e)}")
        processing_results[task_id] = {"status": "error", "message": str(e)}

@router.post("/document-analyze", response_model=DocumentResponse)
@router.post("/document-analyzer", response_model=DocumentResponse)
async def analyze_document(
    request: DocumentRequest, 
    background_tasks: BackgroundTasks,
    x_api_key: str = Header(...)
):
    """Main endpoint for document analysis using background tasks."""
    # 1. Authentication
    expected_api_key = os.getenv("API_KEY", "sk_track2_987654321")
    if x_api_key != expected_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")

    logger.info(f"Received analysis request: file={request.fileName}, type={request.fileType}")
    
    # 2. Generate a task ID
    task_id = str(uuid.uuid4())
    
    # 3. Enqueue the task (Async processing requirement)
    background_tasks.add_task(
        background_processing_task, 
        task_id, 
        request.fileName, 
        request.fileType, 
        request.fileBase64
    )
    
    # 4. Immediate extraction for UI demonstration (Optional)
    # To keep it truly "instant" for the hackathon dashboard, we actually 
    # run the extraction and analysis sync in this thread if we want 
    # the JSON to return immediately.
    # The hackathon spec (aiextracter.txt) implies the POST returns the JSON result directly.
    # SO, we will perform it synchronously but keep the "Background" logic as an option.
    
    try:
        start_time = time.time()
        # TEXT EXTRACTION
        text = process_document(request.fileBase64, request.fileType)
        extract_time = time.time() - start_time
        
        # AI ANALYSIS
        analysis = analyze_content(text)
        total_time = time.time() - start_time
        
        logger.info(f"Analysis complete in {total_time:.2f}s")
        
        return DocumentResponse(
            status="success",
            fileName=request.fileName,
            summary=analysis.get("summary", "N/A"),
            entities=analysis.get("entities", {}),
            sentiment=analysis.get("sentiment", "Neutral")
        )
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
