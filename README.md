# VibeStream: AI Cinema Concierge

VibeStream is an autonomous digital concierge designed to solve "choice paralysis" by replacing rigid genre metadata with a natural language, emotion-driven interface. Built using the modern **Google Gen AI SDK**, it translates abstract user moods into tailored film recommendations validated through real-world live data.

## 🔑 Applied Course Key Concepts

* **Agent System (ADK):** Implemented using the modern `google-genai` Client architecture to define an autonomous system governed by rigorous system instructions.
* **Agent Skills (Tools):** Integrates native **Google Search Grounding** (`types.GoogleSearch()`). The agent dynamically queries the live web to eliminate hallucinations and verify movie streaming availability.
* **Security Features:** Incorporates hardcoded Google AI Safety Settings (`SafetySetting`) to actively filter and block hate speech, harassment, and explicit content.
* **Deployability & Antigravity:** Designed as a lightweight micro-frontend with Streamlit, enabling instant deployment to serverless platforms in under two minutes.


## 🛠️ Installation & Setup

Follow these steps to run the AI Cinema Concierge locally on your machine:

### 1. Prerequisites
Make sure you have **Python 3.10 or higher** installed on your system. You will also need a free API Key from [Google AI Studio](https://aistudio.google.com/).

### 2. Clone the Repository
Open your terminal or command prompt and clone this project:
```bash
git clone https://github.com/tkabbaj/VibeStream-AI-Cinema-Concierge.git
cd VibeStream-AI-Cinema-Concierge
```
*(Note: If you downloaded the project as a ZIP file, just extract it and open your terminal inside that folder).*

### 3. Install Dependencies
Install the required official packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Launch the Application
Run the Streamlit server via Python to initialize the micro-frontend:
```bash
python -m streamlit run app.py
```
*Alternatively, if using Docker:*
```bash
docker build -t vibestream-app .
docker run -p 8501:8501 -e GOOGLE_API_KEY="your_key_here" vibestream-app
```

## 🕹️ How to Use the Agent

1. Once the application launches, your default web browser will automatically open a tab at `http://localhost:8501`.
2. Authentication: 
   - If a GOOGLE_API_KEY is detected via environment variables, the app will initialize directly. 
   - If no key is found, a Configuration sidebar will appear. Paste your API key there to unlock the agent.
3. In the main text area, describe your exact emotional state or aesthetic requirement (e.g., *"An intense 90s thriller space with a rainy neon aesthetic"*).
4. Click **Find My Match** and watch the agent securely fetch, ground, and display exactly 3 tailored cinema recommendations directly from the live web.

## 🚀 Live Demo

[Check out the live app here](https://vibestream-ai-cinema-concierge-ahscmda53p5q2wdlaxx6tk.streamlit.app/)

## ⚙️ Deployment Guide

This project is built to be flexible and highly portable. Choose the method that best fits your environment:

### Option 1: Streamlit Cloud
The fastest way to get VibeStream live in under two minutes:
1. Connect this repository to your [Streamlit Cloud](https://share.streamlit.io/) account.
2. In the app settings, add GOOGLE_API_KEY to the Secrets section.
2. Click **Deploy**.

### Option 2: Google Cloud Run
This project includes a `Dockerfile` for professional, scalable deployments.
1. Ensure the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) is installed.
2. Store your API Key in [Google Secret Manager](https://cloud.google.com/security/products/secret-manager):
   - Create the secret: `gcloud secrets create GOOGLE_API_KEY --replication-policy="automatic"`
   - Add the version: `echo -n "YOUR_API_KEY" | gcloud secrets versions add GOOGLE_API_KEY --data-file=-`
2. Authenticate and set your project:
   ```bash
   gcloud auth login
   gcloud config set project [YOUR_PROJECT_ID]
   gcloud run deploy vibestream --source . --set-secrets GOOGLE_API_KEY=GOOGLE_API_KEY:latest
   ```