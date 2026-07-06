import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="wide"
)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

st.title("🎓 AI Learning Buddy")
st.subheader("Learn any topic with AI")

st.markdown("---")

st.sidebar.title("📚 About")
st.sidebar.write("""
AI Learning Buddy helps you learn **any topic** through:

- 📖 Simple Explanations
- 🌍 Real-Life Examples
- ❓ Quiz Generation
- 🗺️ Learning Roadmap
- 💬 Ask Anything
""")

topic = st.text_input(
    "Enter any topic",
    placeholder="Example: Python, Java, DBMS, AI, Cloud Computing..."
)

activity = st.selectbox(
    "Choose an activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Learning Roadmap",
        "Ask Anything"
    ]
)

if st.button("🚀 Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if activity == "Explain Concept":
            prompt = f"Explain '{topic}' in simple language for a beginner."

        elif activity == "Real-Life Example":
            prompt = f"Give one simple real-life example of '{topic}'."

        elif activity == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions with answers on '{topic}'."

        elif activity == "Learning Roadmap":
            prompt = f"""
Create a complete beginner-friendly roadmap to learn {topic}.

Organize it like this:

📘 Beginner
- Topics to learn

📙 Intermediate
- Topics to learn

📕 Advanced
- Topics to learn

After that include:

✅ One beginner project
✅ One intermediate project
✅ One advanced project

Finally recommend:
- 2 free websites
- 2 YouTube channels
- Estimated time to master the topic
"""

        else:
            prompt = topic

        try:

            response = client.chat.completions.create(
                model="openrouter/auto",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.success("Response Generated Successfully!")

            st.markdown("## 🤖 AI Response")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption("Made with ❤️ using Streamlit and OpenRouter")
