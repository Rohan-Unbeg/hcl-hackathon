"""
AI Analysis Engine.
Powered by Gemini 2.5 Flash for high-speed, high-accuracy document intelligence.
"""

import json
import logging
import os
import google.generativeai as genai

logger = logging.getLogger(__name__)

SYSTEM_INSTRUCTIONS = """
Analyze the provided document text and extract structured information.
Response MUST be a valid JSON object with the following keys:
- summary: A professional 2-3 sentence overview.
- entities: Object containing:
    - names: List of person names.
    - dates: List of specific dates referenced.
    - organizations: List of companies, agencies, or institutions.
    - amounts: List of monetary values (e.g. $500, ₹10k).
- sentiment: Exactly one of ["Positive", "Neutral", "Negative"].

Logic for Sentiment:
- Business reports, technical documents, and factual statements -> Neutral.
- Success stories, growth milestones, positive testimonials -> Positive.
- Incident reports, data breaches, negative reviews -> Negative.

Format only as JSON. No markdown wrappers.
"""


def analyze_content(text: str) -> dict:
    """
    Sends document text to Gemini for structured extraction.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not configured in environment.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config={"response_mime_type": "application/json"}
    )

    prompt = f"{SYSTEM_INSTRUCTIONS}\n\nDOCUMENT TEXT:\n{text}"

    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        logger.error(f"Gemini analysis failed: {e}")
        return {
            "summary": "Error during AI analysis.",
            "entities": {"names": [], "dates": [], "organizations": [], "amounts": []},
            "sentiment": "Neutral"
        }
