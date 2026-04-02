# Deployment Guide: DocIntel // Deep Extraction Engine

To win the hackathon, you must provide a **Live Deployed URL**. This version is optimized for **Render's FREE Tier**.

## 1. Prepare GitHub Repository
If you haven't already:
```bash
git add .
git commit -m "feat: optimized for free-tier deployment"
git push origin main
```

## 2. Deploy on Render.com (Web Service)

### Step A: The API Service (Combined Engine)
1. Go to [dashboard.render.com](https://dashboard.render.com) and click **New > Web Service**.
2. Connect your GitHub repository (`hcl-hackathon`).
3. **Name**: `docintel-api` (or any name you like)
4. **Runtime**: `Python 3`
5. **Build Command**: `pip install --upgrade pip && pip install -r requirements.txt`
6. **Start Command**: `uvicorn src.main:app --host 0.0.0.0 --port $PORT`
7. **Instance Type**: Select **Free** ($0/month).
8. **Environment Variables** (Click Advanced):
   - `PYTHON_VERSION`: `3.10.16` (CRITICAL: Prevents build errors on Render)
   - `GEMINI_API_KEY`: Your Google Gemini key.
   - `API_KEY`: `sk_track2_987654321` (this is the key the GUVI tester will use).

## 3. Verify Public Access
Once deployed, Render will give you a URL like `https://docintel-api.onrender.com`.
1. Test it by visiting the URL in your browser—the **DocIntel Dashboard** should load!
2. Go back to your GUVI hackathon dashboard and use the **Endpoint Tester** with this URL.

## 4. Final Submission
Submit the following to the GUVI portal:
- **Live URL**: Your Render URL.
- **API Key**: `sk_track2_987654321`
- **GitHub Link**: Your GitHub repo link.
