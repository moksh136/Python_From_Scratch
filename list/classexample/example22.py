"""s = input()
n = len(s)
i = -1
while i>=-n:
    print(s[i], end = "")
    i -=1
"""
"""print(chr(65))"""
"""s = input()
res = ""
i = 0
while i < len(s):
    if i == 0 or s[i-1] == " ":
        upper = ord(s[i])-32
        res = res+chr(upper)
    else:
        res+=s[i]
    i+=1
print(res)"""
"""l = list(range(0, 7, 2))
print(l)"""
"""l = [1, 2, 3, 4, 5, 6]
res = []
for i in l :
    if i % 2 == 0:
        res.append(i)
print(res)"""
"""n = int(input())
a = []
for i in range(n):
    x = int(input("enter value:"))
    a.append(x)
print(a)"""
print("for mat 1")
ra = int(input())
ca = int(input())
a = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    a.append(row)
print(a)
print("for mat 2")
r1 = int(input())
c1 = int(input())
b = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    b.append(row)
print(b)
print("null mat")
r2 = int(input())
c2 = int(input())
c = []
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(0)
    c.append(row)
print(c)
for i in range(r):
    for j in range(c):
        c[i][j] = c[i][j]+a[i][j]+b[i][j]
print(c)