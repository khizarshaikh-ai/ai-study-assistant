from difflib import get_close_matches

# Example study data
study_data = {
    "python loops": {
        "content": "Python loops allow repeated execution of code. Examples: for, while.",
        "mcqs": [
            {
                "question": "Which loop is used when number of iterations is known?",
                "options": ["for loop", "while loop", "if statement", "switch"],
                "answer": "for loop"
            },
            {
                "question": "Which loop runs until a condition becomes false?",
                "options": ["for loop", "while loop", "if statement", "break"],
                "answer": "while loop"
            }
        ]
    },
    "variables": {
        "content": "Variables store data in Python. Example: x = 5",
        "mcqs": [
            {
                "question": "Which symbol is used for assignment?",
                "options": ["=", "==", "+=", "-="],
                "answer": "="
            }
        ]
    }
}

# -------------------------------
# Generate study content safely
# -------------------------------
def find_topic(user_input):
    topics = study_data.keys()
    match = get_close_matches(user_input.lower(), topics, n=1, cutoff=0.5)
    if match:
        return match[0]
    return None

def generate_study_content(topic):
    found_topic = find_topic(topic)
    if found_topic:
        return study_data[found_topic]["content"]
    else:
        return "Sorry, content for this topic is not available."

def get_mcqs(topic):
    found_topic = find_topic(topic)
    if found_topic:
        return study_data[found_topic]["mcqs"]
    else:
        return []
