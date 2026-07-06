import streamlit as st

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


def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

load_css()

# ==========================
# Header
# ==========================
st.markdown("<h1>🎓 AI Learning Buddy</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center;color:gray;'>Your Personal AI Learning Platform</p>",
    unsafe_allow_html=True
)

# ==========================
# Metrics
# ==========================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📖 Learning Modes", "10")

with col2:
    st.metric("🤖 AI Powered", "Yes")

with col3:
    st.metric("⚡ Response", "Instant")

st.markdown("---")

# ==========================
# Sidebar
# ==========================
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

# ==========================
# Main Content
# ==========================
st.subheader("📚 Choose a Learning Mode")

activity = st.radio(
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

# Input Field
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

# Generate Button
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

        with st.spinner("🤖 AI is generating your response..."):

            try:

                result = generate_response(prompt)

                st.success("✅ Response Generated Successfully!")

                st.markdown("## 🤖 AI Response")

                st.markdown(
                    f"""
                    <div class="response-card">

                    {result}

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.download_button(
                    label="📥 Download Response",
                    data=result,
                    file_name="AI_Response.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(str(e))

# ==========================
# Footer
# ==========================
st.markdown("---")

st.caption("Made with ❤️ using Streamlit + OpenRouter")
