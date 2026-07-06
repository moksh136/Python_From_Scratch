import random

roasts = [
    "Hearing your name instantly reminded me of the assignment.",
    "Itna genius naam, itna kam padhai?",
    "You show up in class less often than your attendance record does. 😅"
]

compliments = [
    "Your name itself is a whole vibe. ✨",
    "Meeting you made my day!😊",
    "You're definitely topper material! 🔥"
]

def get_roast(name):
    return f"{name}, {random.choice(roasts)}"

def get_compliment(name):
    return f"{name}, {random.choice(compliments)}"