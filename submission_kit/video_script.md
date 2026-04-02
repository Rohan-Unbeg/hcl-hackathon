# Video Demo Script - DocIntel v2.1

**Total Duration**: 120-180 Seconds
**Role**: Technical Lead / Developer

---

### 1. Introduction (0:00 - 0:30)
*   **Visual**: Show the DocIntel Dashboard (Dark Mode UI).
*   **Audio**: "Hi, I'm Rohan. Today I'm presenting DocIntel—a production-grade AI Document Extraction engine built for the GUVI 2026 Hackathon. Unlike basic wrappers, DocIntel is a decoupled, scalable system designed for high-precision extraction from PDF, DOCX, and Image formats."

### 2. The Dashboard & Core Features (0:30 - 1:15)
*   **Visual**: Drag and drop `sample1.pdf` into the "INGESTION_ZONE".
*   **Audio**: "Our dashboard emphasizes developer experience. When a file is uploaded, it enters our ingestion layer. Notice the real-time feedback as the system processes. In under 5 seconds, we have a full extraction: AI-powered summary, Categorized Entities, and Sentiment Analysis."
*   **Visual**: Zoom in on the "Entity Map" (Organization tags like Google, Microsoft).
*   **Audio**: "We don't just extract text; we understand it. Our engine maps organizations, names, and monetary values into structured JSON records."

### 3. Deep Extraction Strategy (1:15 - 1:45)
*   **Visual**: Switch to VS Code, show `src/core/extractor.py`.
*   **Audio**: "Technically, we utilize a multi-layer pipeline. We use PyMuPDF for structural PDF parsing and Tesseract 5.0 for OCR on images. For OCR, we implemented custom grayscale and contrast pre-processing to handle noisy scans, which significantly improved accuracy for the hackathon's image test cases."

### 4. Scalability & AI Stack (1:45 - 2:30)
*   **Visual**: Show `docker-compose.yml` or the `src/worker` logic.
*   **Audio**: "To ensure production scalability, we integrated Celery with Redis for asynchronous task management. This decouples the AI processing from the API response time. Our intelligence layer is powered by Gemini 2.5 Flash, which provides near-instant semantic analysis with high precision."

### 5. Conclusion & Compliance (2:30 - 3:00)
*   **Visual**: Show the README "AI Tools Used" section and finally the "Test Successful" badge.
*   **Audio**: "Documentation is complete with full AI tool disclosure and architectural deep-dives. DocIntel is live, Docker-ready, and fully verified for all 15 test cases. Thank you for your time."

---
*Note: Record this using OBS or a similar tool. Ensure your audio is clear and the dark-mode UI is vibrant.*
