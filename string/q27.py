"""
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:


aabbccdde


Output:


5"""
s = input()
count = 1
first = s[0]
for i in range (1 , len(s)):
    if first == s[i]:
        first = s[i]
    else:
        count+=1
        first = s[i]
print(count)
