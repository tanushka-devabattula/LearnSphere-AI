# ==========================================
# Standard AI Learning Buddy Prompts
# ==========================================

def explain_prompt(topic):
    return f"""
Explain the topic "{topic}" in a beginner-friendly way.

Include:
- Definition
- Why it is important
- Working
- Example
- Interview Tip
"""


def example_prompt(topic):
    return f"""
Give simple real-life examples for:

{topic}

Explain them in easy language.
"""


def quiz_prompt(topic):
    return f"""
Create 10 multiple-choice questions with answers about:

{topic}
"""


def roadmap_prompt(topic):
    return f"""
Create a complete learning roadmap for:

{topic}

Include:
- Beginner
- Intermediate
- Advanced
- Projects
- Resources
"""


def interview_prompt(topic):
    return f"""
Generate interview questions about:

{topic}

Include:
- Beginner
- Intermediate
- Advanced
"""


def summary_prompt(notes):
    return f"""
Summarize these notes.

Include:
- Summary
- Key Points
- Revision Notes

Notes:

{notes}
"""


def flashcard_prompt(topic):
    return f"""
Create 15 flashcards for:

{topic}

Format:

Question:
...

Answer:
...
"""


def planner_prompt(goal):
    return f"""
Create a study plan for:

{goal}

Include:
- Daily Tasks
- Weekly Goals
- Revision Plan
"""


def resources_prompt(topic):
    return f"""
Recommend the best resources for learning:

{topic}

Include:
- Documentation
- YouTube
- Courses
- Books
- Practice Websites
"""


def ask_anything_prompt(question):
    return f"""
Answer the following question clearly and accurately:

{question}
"""


# ==========================================
# PDF Features
# ==========================================

def pdf_summary_prompt(text):
    return f"""
Summarize the following PDF notes.

Include:
- Short Summary
- Key Points
- Important Terms
- Revision Notes

PDF Content:

{text}
"""


def pdf_quiz_prompt(text):
    return f"""
Create 10 MCQs with answers from the following PDF notes.

PDF Content:

{text}
"""


def pdf_flashcards_prompt(text):
    return f"""
Create 15 flashcards from the following PDF.

Format:

Question:
...

Answer:
...

PDF Content:

{text}
"""


def pdf_interview_prompt(text):
    return f"""
Generate interview questions from these PDF notes.

Include:
- Beginner
- Intermediate
- Advanced

PDF Content:

{text}
"""
