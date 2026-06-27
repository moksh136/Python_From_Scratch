"""
=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
"""
n = int(input())
d = {}
for i in range(n):
    prod = input()
    quantity = int(input())
    d[prod] = quantity

for k, v in d.items():
    if v<30:
        print(k)