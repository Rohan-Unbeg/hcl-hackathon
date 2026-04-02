#!/usr/bin/env python3
"""
Test script to verify the API with the provided sample files.
Encodes each sample file as base64 and sends it to the API.

Usage:
    source venv/bin/activate
    python test_api.py
"""

import base64
import json
import os
import sys

import requests

API_URL = "http://localhost:8000/api/document-analyze"
API_KEY = "sk_track2_987654321"

SAMPLE_FILES = [
    {
        "path": "samplefilestotest-provided/sample1-Technology Industry Analysis.pdf",
        "fileName": "sample1-Technology Industry Analysis.pdf",
        "fileType": "pdf",
    },
    {
        "path": "samplefilestotest-provided/sample2-Cybersecurity Incident Report.docx",
        "fileName": "sample2-Cybersecurity Incident Report.docx",
        "fileType": "docx",
    },
    {
        "path": "samplefilestotest-provided/sample3.jpg",
        "fileName": "sample3.jpg",
        "fileType": "image",
    },
]

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}


def test_file(sample: dict) -> dict:
    """Test a single file against the API."""
    file_path = sample["path"]

    if not os.path.exists(file_path):
        print(f"  ❌ File not found: {file_path}")
        return None

    # Read and encode file
    with open(file_path, "rb") as f:
        file_base64 = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "fileName": sample["fileName"],
        "fileType": sample["fileType"],
        "fileBase64": file_base64,
    }

    print(f"  📤 Sending request ({len(file_base64)} base64 chars)...")

    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=120)
        print(f"  📥 Status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"  ✅ Success!")
            print(f"     Summary: {data.get('summary', 'N/A')[:100]}...")
            print(f"     Entities: {json.dumps(data.get('entities', {}), indent=2)[:200]}")
            print(f"     Sentiment: {data.get('sentiment', 'N/A')}")
            return data
        else:
            print(f"  ❌ Error: {response.text[:200]}")
            return None

    except requests.exceptions.ConnectionError:
        print("  ❌ Connection failed. Is the server running on localhost:8000?")
        return None
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return None


def main():
    print("=" * 60)
    print("🔬 AI Document Analysis API Tester")
    print("=" * 60)

    # Test health endpoint first
    try:
        health = requests.get("http://localhost:8000/health", timeout=5)
        print(f"\n🏥 Health Check: {health.json()}")
    except Exception:
        print("\n❌ Server is not running! Start it with:")
        print("   source venv/bin/activate && python -m src.main")
        sys.exit(1)

    results = []
    for i, sample in enumerate(SAMPLE_FILES, 1):
        print(f"\n{'─' * 60}")
        print(f"📄 Test {i}/3: {sample['fileName']} ({sample['fileType']})")
        print(f"{'─' * 60}")
        result = test_file(sample)
        results.append(result)

    # Summary
    print(f"\n{'=' * 60}")
    print(f"📊 Results: {sum(1 for r in results if r)} / {len(results)} passed")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
