"""
Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a
"""
s = input("Enter String: ")

found_char = ""

for i in range(len(s) - 1, -1, -1):
    current_char = s[i]
    
    count = 0
    for j in range(len(s)):
        if s[j] == current_char:
            count = count + 1
            
    if count > 1:
        found_char = current_char
        break 

if found_char != "":
    print("Output is :", found_char)
else:
    print("No repeating character found")