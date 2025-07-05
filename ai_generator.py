import google.generativeai as genai

# Put your Gemini API key here
API_KEY = "AIzaSyC2-_vHN8lM1403nyQDnQsJ37e05Ne3oy8"

def init_gemini():
    """
    Initialize Gemini client with the fixed API key.
    """
    genai.configure(api_key=API_KEY)

def get_finance_tip(topic=None):
    """
    Ask Gemini 1.5 Flash for a personal finance tip and initial steps.
    If a topic is given, generate a tip about that topic.
    Otherwise, generate a random tip.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")

    if topic:
        prompt = (
            f"Give me a simple, practical, and actionable personal finance tip "
            f"about {topic}. Keep it short and easy to understand. "
            f"Then, list 2-3 initial steps to get started with this tip."
        )
    else:
        prompt = (
            "Give me a simple, practical, and actionable personal finance tip "
            "on any topic. Keep it short and easy to understand. "
            "Then, list 2-3 initial steps to get started with this tip."
        )

    response = model.generate_content(prompt)
    return response.text.strip()
