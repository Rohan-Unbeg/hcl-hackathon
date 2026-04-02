"""
Celery Task Definitions for Scalability.
"""
from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "doc_extraction",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)


@celery_app.task(name="process_doc_async")
def process_doc_async(file_base64: str, file_type: str):
    """
    Background worker task for document processing.
    """
    from src.core.extractor import process_document
    from src.core.analyzer import analyze_content

    text = process_document(file_base64, file_type)
    return analyze_content(text)
