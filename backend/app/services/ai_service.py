import os
import requests
import openai
from dotenv import load_dotenv

# Load environmental configurations
load_dotenv()

AI_MODEL = os.getenv("AI_MODEL", "GoogleGemini")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", os.getenv("GOOGLE_API_KEY"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def call_gemini(prompt: str) -> str:
    """Invokes Google Gemini 2.0 API using lightweight requests."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable is not set")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    response = requests.post(url, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
    response_json = response.json()
    
    try:
        return response_json["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        raise ValueError("Failed to parse response structure from Gemini API")


def call_openai(prompt: str) -> str:
    """Invokes OpenAI ChatCompletion API using legacy SDK wrapper."""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        timeout=10
    )
    return response["choices"][0]["message"]["content"]


def get_simulated_recommendation(prompt: str) -> str:
    """Generates context-aware cognitive accessibility insights for demo/offline use."""
    lower_prompt = prompt.lower()
    
    if "routine" in lower_prompt or "schedule" in lower_prompt or "task" in lower_prompt:
        return (
            "🧠 [Neuro-Assist AI Routine Insight]\n"
            "To support your executive functioning, we recommend breaking your routine down into distinct "
            "15-minute segments. Incorporate visual anchors (e.g., color-coded schedules) and set soft-tone "
            "IoT alarms 5 minutes before transitions to avoid attention-switching friction."
        )
    elif "learn" in lower_prompt or "study" in lower_prompt or "course" in lower_prompt:
        return (
            "📚 [Neuro-Assist AI Learning Guide]\n"
            "This concept is best absorbed through spatial mapping and visual flowcharts. Avoid long "
            "monolithic paragraphs. We recommend reviewing in 25-minute Pomodoro blocks followed by "
            "non-screen relaxation intervals to aid memory consolidation."
        )
    elif "job" in lower_prompt or "career" in lower_prompt or "work" in lower_prompt:
        return (
            "💼 [Neuro-Assist AI Career Guidance]\n"
            "Based on your profile, structured work environments with clear milestone specifications and "
            "asynchronous communication channels will optimize your output. Look for roles with adaptive "
            "workstations or flexible hours."
        )
    elif "mood" in lower_prompt or "feel" in lower_prompt or "anxious" in lower_prompt or "health" in lower_prompt:
        return (
            "💙 [Neuro-Assist AI Wellbeing Companion]\n"
            "A shift in cognitive energy is detected. We suggest pausing to practice a 4-7-8 breathing exercise "
            "to down-regulate your autonomic nervous system. Consider logging a mindfulness entry in your journal "
            "to visually chart this emotional wave."
        )
    
    return (
        "✨ [Neuro-Assist AI Tailored Assistance]\n"
        "To optimize cognitive load, we recommend isolating this topic into three single-focus tasks. "
        "Eliminate sensory clutter in your physical workstation, and introduce active retrieval techniques "
        "when exploring new concepts."
    )


def analyze_text(input_text: str) -> str:
    """
    Core AI entry point to process text prompts.
    Robustly handles various model configs and fails gracefully to high-quality fallback simulations.
    """
    model_choice = AI_MODEL.strip().lower()
    
    try:
        if model_choice in ["googlegemini", "gemini", "google"]:
            print(f"[AI SERVICE] Querying Google Gemini 2.0 API...")
            return call_gemini(input_text)
        elif model_choice in ["openai", "gpt-4", "gpt"]:
            print(f"[AI SERVICE] Querying OpenAI API...")
            return call_openai(input_text)
        else:
            print(f"[AI SERVICE] Unsupported model choice '{AI_MODEL}'. Using simulation...")
            return get_simulated_recommendation(input_text)
            
    except Exception as e:
        print(f"[AI SERVICE WARNING] API execution failed: {e}. Falling back to simulated recommendation...")
        return get_simulated_recommendation(input_text)
