"""
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password"""
password = input("Enter password: ")

special_chars = "@#$%&*"

digit_count = 0
special_count = 0

for ch in password:
    if ch.isdigit():
        digit_count += 1
    if ch in special_chars:
        special_count += 1

if (
    password[0].isupper() and
    password[-1].isdigit() and
    digit_count >= 2 and
    special_count >= 1 and
    " " not in password and
    8 <= len(password) <= 15
):
    print("Secure Password")
else:
    print("Weak Password")