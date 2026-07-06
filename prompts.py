def flashcard_prompt(topic):
    return f"""
Create 15 flashcards for {topic}.

Format exactly like this:

🃏 Flashcard 1

Question:
...

Answer:
...

--------------------

🃏 Flashcard 2

Question:
...

Answer:
...

Continue until 15 flashcards.
"""


def planner_prompt(topic):
    return f"""
Create a 30-day study plan for learning {topic}.

For each day include:
- Topic
- Practice Task

End with:
- Mini Project
- Final Project
- Interview Preparation Tips
"""


def resources_prompt(topic):
    return f"""
Recommend the best FREE resources to learn {topic}.

Include:

📚 Websites

🎥 YouTube Channels

📖 Documentation

💻 Practice Platforms

Mention why each resource is useful.
"""
