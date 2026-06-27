"""
Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
"""
a = input("Enter feedback message: ")

count = 0

for ch in a:
    if ch in "aeiou" or "AEIOU":
        count += 1

print("Total vowels:", count)

