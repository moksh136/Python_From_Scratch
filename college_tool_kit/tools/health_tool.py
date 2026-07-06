import math

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / math.pow(height_m, 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal / Healthy"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def health_tip(category):
    tips = {
        "Underweight": "You should eat a bit more, buddy—focus on getting enough protein! 🍗",
        "Normal / Healthy": "You're absolutely right! Keep it up like this 💪",
        "Overweight": "Start some walking/exercise and reduce fast food.",
        "Obese": "It would be better to consult a doctor; follow a healthy diet 🥗"
    }
    return tips.get(category, "Stay healthy!")