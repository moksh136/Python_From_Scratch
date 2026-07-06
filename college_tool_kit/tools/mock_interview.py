import random

questions = [
    {"q": "what is output of 5>3>1", "options": ["True", "False", "5 > (3 > 1)"], "answer": "True"},
    {"q": "who is the creator of python?", "options": ["Guido van Rossum", "Elon Musk", "Bill Gates"], "answer": "Guido van Rossum"},
    {"q": "What is the output of print(True + True)", "options": ["True", "2", "1"], "answer": "2"},
    {"q": "What is the output of: print(10 / 3", "options": ["3", "3.0", "3.3333333"], "answer": "3.3333333"},
    {"q": "what is the full form pf HTML?", "options": ["HyperText Markup Language", "High Text Machine Language", "None"], "answer": "HyperText Markup Language"}
]

def get_random_questions(count=3):
    return random.sample(questions, count)

def check_answer(question, user_answer):
    return question["answer"].lower() == user_answer.lower()

def run_mock():
    selected = get_random_questions(3)
    score = 0
    for q in selected:
        print(f"\n{q['q']}")
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        user_input = input("type your answer: ")
        if check_answer(q, user_input):
            print("Correct! ✅")
            score += 1
        else:
            print(f"wrong! the correct answer is: {q['answer']} ❌")
    return score