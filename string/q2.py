"""
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5"""
a = input("Enter feedback message: ")

count = 0
for ch in a:
    if ch == " ":
        count+=1
print(count)