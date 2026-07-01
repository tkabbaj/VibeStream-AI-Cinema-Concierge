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
git clone [https://github.com/tkabbaj/VibeStream-AI-Cinema-Concierge.git](https://github.com/tkabbaj/VibeStream-AI-Cinema-Concierge.git)
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
python -m streamlit run app.p
```

## 🚀 How to Use the Agent

1. Once the application launches, your default web browser will automatically open a tab at `http://localhost:8501`.
2. Locate the **Configuration** section in the left sidebar and paste your **Google AI Studio API Key**.
3. In the main text area, describe your exact emotional state or aesthetic requirement (e.g., *"An intense 90s thriller space with a rainy neon aesthetic"*).
4. Click **Find My Match** and watch the agent securely fetch, ground, and display exactly 3 tailored cinema recommendations directly from the live web.
