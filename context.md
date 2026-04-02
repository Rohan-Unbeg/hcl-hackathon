This is a empty project folder for hcl hackathon

context - from official site


rohanunbeg0918@gmail.com


Dashboard

Timeline

Hackathon Challenge
GUVI Hackathon 2026 - Intern Hiring
GUVI Hackathon 2026 challenges developers to build production-quality applications over an intensive sprint. Participants choose one of three engineering tracks and deliver a fully functional, hosted solution. Each track is scored out of 100 points with optional bonus points available.

Challenge Levels
Complete each level to advance in the hackathon

0%
Level 1 - Problem Statement Selection

Active


This is the first step of your hackathon journey, where you will explore and select a problem statement to work on. The hackathon is designed to encourage participants to solve real-world challenges by building innovative, practical, and scalable solutions using technology.

Rules

Only one problem statement can be selected.
Custom or alternate problem statements are not allowed.
Once selected, the problem statement cannot be changed later.
Make sure to select your problem statement within the given time window. The selection portal will open at the specified start time and will close when the deadline is reached.
If you do not select a problem statement before the deadline, you will not be allowed to proceed to the next stage of the hackathon.
Starts at:
01 Apr 2026, 10:00:00 AM

Ends at:
04 Apr 2026, 11:59:00 PM

Select Problem Statement
AI-Powered Document Analysis & Extraction – API Endpoint Tester

Locked


Call Compliance – API Endpoint Tester

Locked


Level 2 - Form Submission

Locked




rohanunbeg0918@gmail.com


Dashboard

Timeline

Level 1 - Problem Statement Selection
Select a problem statement to begin your hackathon journey

3
Problems
Available Problem Statements
Call Center Compliance

108/2000 Enrolled

Available

Problem Description

Build an intelligent call centre analytics system that processes voice recordings in Hindi (Hinglish) and Tamil (Tanglish), extracts text using speech-to-text, validates calls against standard operating procedures (SOP), and categorises payment preferences.

Key Features

Voice-to-Text Processing — extract text from Hindi (Hinglish) & Tamil (Tanglish) calls
Text Summarisation — AI-powered summary of extracted call content
SOP Validation — validate calls against standard script templates
Payment Categorisation — count and categorise EMI, Full Payment, Partial Payment, Down Payment
Rejection Analysis — extract and categorise reasons for rejection from call text
Technical Requirements

Speech-to-Text: Flexible model (supports Hindi & Tamil)
AI/ML: Flexible model for text summarisation and entity extraction
Backend: Any language with Celery for async voice processing
Submission Requirements

Live deployed URL (must be publicly accessible)
API Key
GitHub repository link
Reference Documents

Sample Audio to test: https://recordings.exotel.com/exotelrecordings/guvi64/5780094ea05a75c867120809da9a199f.mp3
Refer this document: Call Center Compliance
Note: The detailed evaluation process, request/response format, scoring logic, and technical requirements are explained in the respective reference documents.

Scoring Rubric — 100 Points

API Functionality & Accuracy — 90 Points

The API will be tested using 10 audio files, each representing one test case worth 100 points. Each API response will be evaluated based on the following components.
Response Structure — 20 pts
Transcript & Summary— 30 pts
SOP Validation — 30 pts
Analytics — 10 pts
Keywords — 10 pts
With 10 test cases, the maximum raw score is 1000.
Final Score Formula: Final Score = (Total Score from 10 Tests / 1000) × 90
GitHub Repository Code Quality — 10 Points

Code structure and readability
Features & Functionality
Technical Implementation
No Hardcoded Responses

Select Problem Statement
Real-time Collaborative Text Editor

109/2000 Enrolled

Available

Problem Description

Build a real-time collaborative text editor where multiple users can edit the same document simultaneously — think Google Docs, but simpler. Changes must sync instantly across all connected users with robust conflict resolution.

Key Features

Real-time synchronisation of text changes across multiple users
User presence indicators — show who is online and currently editing
Cursor position tracking per user (coloured cursors)
Conflict resolution when multiple users edit the same section
Basic text formatting: bold, italic, underline
Document persistence and revision history
Technical Requirements

WebSocket-based real-time communication
Operational Transformation (OT) or Conflict-free Replicated Data Types (CRDTs)
Backend: Node.js / Python with WebSocket support
Frontend: React / Vue.js with collaborative editing libraries
Database: PostgreSQL / MongoDB for document storage
Submission Requirements

Live deployed URL (must be publicly accessible)
GitHub repository link
Video Demo URL (Youtube/Google Drive Link)
Scoring Rubric — 100 Points

Code Quality & Structure (25 Points) - Clean, readable, modular code; meaningful git history; no hardcoded secrets; proper error handling
Features & Functionality (30 Points) - All required features working; real-time sync reliable under multi-user load; document persistence
Technical Implementation (25 Points) - Correct use of WebSockets + OT/CRDT; proper conflict resolution; scalable architecture choices
User Experience & Design (20 Points) - Polished UI; responsive layout; intuitive user presence indicators; smooth editing UX

Select Problem Statement
AI-Powered Document Analysis & Extraction

221/2000 Enrolled

Available

Problem Description

Create an intelligent document processing system that can extract, analyse, and summarise content from various document formats (PDF, DOCX, image with text). The system must leverage AI to understand document structure and extract key information automatically.

Key Features

Multi-format support: PDF, DOCX, and image (via OCR)
Automatic text extraction with layout preservation
AI-powered summarisation
Key entity extraction: names, dates, organisations, monetary amounts etc.
Sentiment analysis for text content
Technical Requirements

OCR: Tesseract / Google Cloud Vision API
AI/ML: Flexible model for summarisation
Backend: Any language for async processing
Submission Requirements

Live deployed URL (must be publicly accessible)
API Key
GitHub repository link
Reference Documents

Sample Files to test: https://drive.google.com/drive/folders/1Biiy_gp_jHGfXwccFekqOu1txab9u9zM
Refer this document: AI-Powered Document Analysis & Extraction
Note: The detailed evaluation process, request/response format, scoring logic, and technical requirements are explained in the respective reference documents.

Scoring Rubric — 100 Points

API Functionality & Accuracy — 90 Points

The API will be evaluated using 15 test cases consisting of 5 PDF files, 5 DOCX files, and 5 images containing text. Each file will be sent to the API for processing, and the response will be analyzed based on the quality and accuracy of the extracted information.Each test case carries 10 points, divided into the following components.
Summary — 2 points (The API should generate a concise and accurate summary of the content.)
Entities — 4 points (The API should correctly extract named entities such as people, organizations, locations, or other relevant entities present in the text.)
Sentiment — 4 points (The API should correctly classify the overall sentiment of the content as positive, negative, or neutral.)
Since there are 15 test cases, the maximum raw score is 150 points. This raw score will then be scaled down to a final score out of 90 points for the API functionality and accuracy evaluation.
Final Score Formula: Final Score = (Total Score from 15 Tests / 150) × 90


GitHub Repository Code Quality —10 Points

Code structure and readability
Features & Functionality
Technical Implementation
No Hardcoded responses

Select Problem Statement

