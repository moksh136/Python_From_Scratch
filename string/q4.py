"""
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11"""
a = input("Enter student name: ")

count = 0

for ch in a.lower():

    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Total consonants:", count)