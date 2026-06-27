"""
Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d"""
s = input("Enter String: ")

max_freq = 0
result = ""

for ch in s:
    # 1. Count how many times 'ch' appears
    count = 0
    for i in range(len(s)):
        if s[i] == ch:
            count = count + 1
            
    if count > max_freq:
        max_freq = count
        result = ch + " "
        
    elif count == max_freq:
        already_exists = False
        for j in range(len(result)):
            if result[j] == ch:
                already_exists = True
                
        if not already_exists:
            result = result + ch + " "

print("Output:", result)