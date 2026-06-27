"""
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india"""
s = input()
words = s.split()
for ch in words:
    word = ch
    count = 0
    for i in range (0, len(words)):
        if word == words[i]:
            count+=1
    if count > 1:
        print(word)