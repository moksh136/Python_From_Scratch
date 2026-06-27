"""4.
=========================================
STUDENT GRADE ANALYSIS
======================
Store student marks in a dictionary.
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
Write a program to:
* Find the student with highest marks.
* Find the student with lowest marks.
Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65"""
n = int(input())
d = {}
for i in range(n):
    name = input("enter name:")
    marks = int(input("enter marks:"))
    d[name] = marks
print(d)
print(max(d.values()))
print(min(d.values()))