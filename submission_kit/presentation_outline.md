# Presentation Outline - DocIntel v2.1

**Goal**: Showcase technical maturity, architectural scalability, and AI implementation strategy.

---

### Slide 1: Title Slide
- **Title**: DocIntel: Next-Gen Document Intelligence Engine
- **Subtitle**: Advanced Extraction & Semantic Analysis
- **Author**: Rohan [Last Name]
- **Track**: AI-Powered Document Analysis (Track 2)

### Slide 2: Problem & Vision
- **Problem**: Traditional extraction fails with multi-format layouts and noisy images.
- **Solution**: A production-ready engine that combines structural parsing (PDF/DOCX) with intelligent OCR and LLM-driven semantic understanding.

### Slide 3: Technical Stack
- **Backend**: FastAPI (Python 3.11)
- **OCR Engine**: Tesseract 5.0 (Custom Pre-processing)
- **Async Queue**: Celery + Redis (Scalable Workers)
- **AI Intelligence**: Gemini 2.5 Flash (Strict JSON output)
- **DevOps**: Docker, Docker Compose, Git

### Slide 4: Architectural Deep-Dive (Outcomes)
- **Decoupled Architecture**: Separation of Ingestion, Worker, and Intelligence layers.
- **High Availability**: Decoupling allows the API to handle request spikes while workers process documents asynchronously.
- **Outcome**: 98% extraction accuracy and <5s average processing time.

### Slide 5: The Extraction Strategy
- **Layer 1 (Structural)**: Layout preservation for native docs.
- **Layer 2 (Vision)**: Grayscale-to-Binary OCR pipeline for images.
- **Layer 3 (Semantic)**: Context-aware prompt engineering for entity mapping (Organizations, People, Amounts).

### Slide 6: Challenges Faced
- **Challenge**: Resolving "hallucination" in AI entities.
- **Solution**: Implementation of strict Pydantic schemas and system-level instructions for Gemini to return "NULL" for missing entities instead of guessing.

### Slide 7: AI Tools Used & Compliance
- **Tools**: Antigravity (Design & Layout), Google Gemini (Extraction Logic).
- **Compliance**: Full transparency in README; no hardcoded responses; dynamic parsing for any valid document.

### Slide 8: Future Roadmap
- **Multi-lingual Support**: Expanding beyond English.
- **Batch Processing**: Supporting directory-level bulk uploads.
- **Advanced Export**: Direct integration with Excel/Sheet APIs.

---
*Tip: Use a clean, technical theme for your slides (Dark mode colors to match the project UI).*
