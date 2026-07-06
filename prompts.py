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
