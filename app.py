import streamlit as st
from google import genai
from google.genai import types

# 1. UI Configuration
st.set_page_config(page_title="VibeStream - AI Cinema Concierge", layout="centered")

st.title("VibeStream")
st.subheader("Your AI Cinema Concierge")
st.write("Ditch rigid category grids. Describe your exact emotional state or vibe, and let the agent search the web.")

# Sidebar configuration for authentication
st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter Google AI Studio API Key:", type="password")

if not api_key:
    st.info("Get a free API Key from Google AI Studio and paste it in the sidebar to initialize the agent.")
else:
    # Initialize Google Gen AI Client (ADK Core Setup)
    client = genai.Client(api_key=api_key)
    
    # [CONCEPT: SYSTEM INSTRUCTIONS / ADK ROLE]
    system_instruction = """
    You are VibeStream, a professional cultural concierge. Your goal is to solve choice paralysis.
    - Translate abstract user inputs (moods, aesthetic descriptions) into film choices.
    - You MUST use the Google Search Tool to verify movie data and active streaming platforms.
    - Output exactly 3 distinct recommendations with Title (Year), a brief custom reasoning, and platforms.
    - Avoid any emojis or visual icons in your final response. Keep the formatting clean and text-based.
    """
    
    # [CONCEPT: SECURITY FEATURES]
    safety_settings = [
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        ),
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
    ]

    # [CONCEPT: AGENT SKILLS] - Native Google Search Tool
    search_tool = types.Tool(
        google_search=types.GoogleSearch()
    )

    # User text area input for the requested vibe
    vibe_input = st.text_area(
        "What is your vibe right now?", 
        placeholder="Example: A cozy rainy Sunday, melancholic neon lights, or an intense 90s thriller space...",
        max_chars=300
    )

    if st.button("Find My Match"):
        if vibe_input:
            with st.spinner("The agent is executing its search skill and evaluating safety parameters..."):
                try:
                    config = types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        tools=[search_tool],
                        safety_settings=safety_settings,
                    )
                    
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=vibe_input,
                        config=config,
                    )
                    
                    st.success("Recommendations Generated Safely:")
                    st.divider()
                    st.markdown(response.text)
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please describe your vibe first.")