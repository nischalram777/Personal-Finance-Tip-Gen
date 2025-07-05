import streamlit as st
from ai_generator import init_gemini, get_finance_tip

# Initialize Gemini
init_gemini()

st.set_page_config(page_title="Personal Finance Tip Generator 💸", page_icon="💸")

st.title("💸 Personal Finance Tip Generator")
st.write("Get a simple, actionable tip to improve your personal finances, along with initial steps to get started!")

option = st.radio(
    "What do you want?",
    ("🎲 Random tip", "📝 Tip on a specific topic")
)

topic = ""
if option == "📝 Tip on a specific topic":
    topic = st.text_input("Enter a topic (e.g., saving, investing, budgeting)")

if st.button("🎯 Get a Finance Tip"):
    with st.spinner("Generating tip..."):
        try:
            tip = get_finance_tip(topic if topic else None)
            st.success("Here’s your tip with initial steps:")
            st.markdown(f"{tip}")
        except Exception as e:
            st.error(f"Error: {e}")

st.caption("Powered by Gemini 1.5 Flash and Streamlit.")
