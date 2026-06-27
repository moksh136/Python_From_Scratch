"""=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi
"""
n = int(input())
res = {}
for i in range(n):
    name = input("enter name:")
    marks = int(input("enter marks:"))
    res[name] = marks
print(res)
for k,v in res.items():
    if v > 50 :
        print(k)