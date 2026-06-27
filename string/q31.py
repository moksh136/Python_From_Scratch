"""
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc
"""
s = input()
res = ""
for i in range (0 , len(s)):
    if s[i] in res:
        break
    else:
        res += s[i]
print(res)
        

