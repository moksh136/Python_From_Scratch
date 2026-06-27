"""
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you


Output:


hello how are you"""
s = input()
words = s.split()
res = words[0]
first = words[0]
for i in range (0 , len(words)):
    if first != words[i]:
        res=res+" "+words[i]
        first = words[i]
    else:
        continue
print(res)
