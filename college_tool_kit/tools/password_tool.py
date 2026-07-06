import string

def has_number(password):
    return any(char.isdigit() for char in password)

def has_symbol(password):
    symbols = string.punctuation
    return any(char in symbols for char in password)

def calculate_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if has_number(password):
        score += 1
    if has_symbol(password):
        score += 1
    return score