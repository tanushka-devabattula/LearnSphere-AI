import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
from prompts import (
    explain_prompt,
    example_prompt,
    quiz_prompt,
    roadmap_prompt,
    interview_prompt,
    summary_prompt,
    flashcard_prompt,
    planner_prompt,
    resources_prompt
)

from utils import generate_response


st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

load_css()

st.markdown("<h1>🎓 AI Learning Buddy</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:gray;'>Your Personal AI Learning Platform</p>",
    unsafe_allow_html=True
)
st.markdown("---")

st.sidebar.title("📚 Features")

st.sidebar.markdown("""
📖 Explain Concept

🌍 Real-Life Example

❓ Generate Quiz

🗺️ Learning Roadmap

💼 Interview Questions

📝 Notes Summarizer

🧠 Flashcards

📅 Study Planner

📚 Learning Resources

💬 Ask Anything
""")

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Learning Roadmap",
        "Interview Questions",
        "Notes Summarizer",
        "Flashcards",
        "Study Planner",
        "Learning Resources",
        "Ask Anything"
    ]
)

if activity == "Notes Summarizer":

    user_input = st.text_area(
        "Paste your notes",
        height=250
    )

else:

    user_input = st.text_input(
        "Enter Topic",
        placeholder="Example: Python, AI, DBMS..."
    )

if st.button("🚀 Generate"):

    if user_input.strip() == "":

        st.warning("Please enter input.")

    else:

        if activity == "Explain Concept":
            prompt = explain_prompt(user_input)

        elif activity == "Real-Life Example":
            prompt = example_prompt(user_input)

        elif activity == "Generate Quiz":
            prompt = quiz_prompt(user_input)

        elif activity == "Learning Roadmap":
            prompt = roadmap_prompt(user_input)

        elif activity == "Interview Questions":
            prompt = interview_prompt(user_input)

        elif activity == "Notes Summarizer":
            prompt = summary_prompt(user_input)

        elif activity == "Flashcards":
            prompt = flashcard_prompt(user_input)

        elif activity == "Study Planner":
            prompt = planner_prompt(user_input)

        elif activity == "Learning Resources":
            prompt = resources_prompt(user_input)

        else:
            prompt = user_input

        with st.spinner("Generating..."):

            try:

                result = generate_response(prompt)

                st.success("Done!")

                st.markdown("## 🤖 AI Response")

                st.write(result)

                st.download_button(
                    "📥 Download Response",
                    result,
                    file_name="AI_Response.txt"
                )

            except Exception as e:

                st.error(str(e))

st.markdown("---")

st.caption("Made with ❤️ using Streamlit + OpenRouter")
