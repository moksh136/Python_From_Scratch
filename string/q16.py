"""
 Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST"""
s = input()
s = s.split()
res = ""
for i in range (0, len(s)):
    a = s[i]
    if "a"<=a[0]<="z":
        cap = chr(ord(a[0])-32)
        res = res+cap
    else:
        res+=a[0]
print(res)

