def explain_prompt(topic):
    return f"""
Explain {topic} in beginner-friendly language.

Include:
- Definition
- Why it is important
- Key points
- Advantages
- Applications

Use simple English.
"""


def example_prompt(topic):
    return f"""
Give 5 simple real-life examples of {topic}.

Explain each example briefly.
"""


def quiz_prompt(topic):
    return f"""
Create 10 multiple-choice questions on {topic}.

Each question must contain:

A)
B)
C)
D)

Mention the correct answer after every question.
"""


def roadmap_prompt(topic):
    return f"""
Create a complete roadmap for learning {topic}.

Format:

📘 Beginner

📙 Intermediate

📕 Advanced

Projects:
- Beginner Project
- Intermediate Project
- Advanced Project

Recommend:
- 2 Websites
- 2 YouTube Channels
- Estimated time required.
"""


def interview_prompt(topic):
    return f"""
Prepare interview questions on {topic}.

Include:

🟢 Beginner Questions (10)

🟡 Intermediate Questions (10)

🔴 Advanced Questions (10)

💻 Coding Questions (if applicable)

⭐ Interview Tips

📚 Best Resources
"""


def summary_prompt(notes):
    return f"""
Summarize the following notes.

Provide:

📌 Short Summary

✅ Key Points

📝 Revision Notes

📚 Important Terms

❓5 Practice Questions

Notes:

{notes}
"""
