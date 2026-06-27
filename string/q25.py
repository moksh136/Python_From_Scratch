"""
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:
e
"""
s = input()
i = 0
f = 0
while i <len(s):
    count = 0
    j = 0 
    while j < len(s):
        if s[i]==s[j]:
            count+=1
        j+=1
    if count==1:
        print(s[i])
        f=1
        break
    i+=1
if f==0:
    print("not found")