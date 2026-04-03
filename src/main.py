"""
DocIntel API // Entry Point
High-performance document extraction & analysis system.
"""

import logging
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.api.routes import router as api_router

# Initialize environment
load_dotenv()

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DocIntel API",
    description="Intelligent Document Extraction Engine",
    version="2.1.0"
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
logger.info("Registering API routes under /api prefix")
app.include_router(api_router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# Static Dashboard (UI)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    logger.info(f"System boot sequence complete. Launching on port {port}")
    uvicorn.run("src.main:app", host="0.0.0.0", port=port, reload=True)
