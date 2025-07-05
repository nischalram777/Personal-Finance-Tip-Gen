# 💸 Personal Finance Tip Generator using Gemini AI

This project is a simple Streamlit-based web app that uses **Google's Gemini 1.5 Flash** model to generate personal finance tips. Users can receive either a random tip or a tip focused on a specific topic like saving, budgeting, or investing.

---

## 👤 Author

**Vaddi Nischal Ram**  
📧 vaddinischal.ram2023@vitstudent.ac.in

---

## 🚀 Features

- 🎲 Get random personal finance tips
- 📝 Ask for tips on specific topics (e.g., "saving", "investing")
- ✅ Practical, short, and easy-to-understand tips
- 🛠 Initial steps included to help users get started
- ⚡ Powered by Gemini 1.5 Flash
- 🌐 Built with Streamlit

---

## 🛠️ Tech Stack

- Python 3.x  
- [Streamlit](https://streamlit.io) for frontend  
- [Google Generative AI (Gemini)](https://ai.google.dev) for tip generation

---

## 📦 Setup Instructions
1. Clone the Repository
git clone https://github.com/nischalram777/Personal-Finance-Tip-Gen
cd finance-tip-generator

2. Install Dependencies
Create a virtual environment (optional):
python -m venv venv
source venv/bin/activate  # On Windows use venv\\Scripts\\activate
Install the required libraries:
pip install -r requirements.txt

3. Add Your Gemini API Key
Open ai_generator.py and replace the API_KEY placeholder with your own Gemini API key:
API_KEY = "your-own-api-key-here"
You can get your API key from: https://makersuite.google.com/app/apikey

4. Run the App
streamlit run app.py
🧠 Example Prompts
🎯 Random Tip:

"Give me a personal finance tip on any topic..."

✍️ Specific Topic ("Investing"):

"Give me a practical investing tip with 2–3 steps to begin."

📈 Future Enhancements
Allow exporting tips to PDF or clipboard

Add voice input for accessibility

Tip saving history for the user

Categorized dashboard view (Tips by type)
