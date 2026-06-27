#149 Check if two strings are scrambled versions of each other
"""s1 = input()
s2 = input()

if sorted(s1)==sorted(s2):
    print("yes")
else:
    print("no")"""
#71Print all substrings
"""s = input()
n = int(input())
for i in range(len(s)-n+1):
    print(s[i:i+n])"""
#71Print all substrings.
"""s = input()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])"""
#73Find the longest palindromic substring
#
#Print ASCII value of each character.
"""a = input()
for i in a:
    print(ord(i))"""
#85Convert string into a char array without built-in functions
"""s= input()
l =[]
for i in s:
    l.append(i)
print(l)"""
#89Remove 'b' and 'a' from a string.
"""s = input()
res = ""
for i in s:
    if i != "b" and i!="a":
        res+=i
print(res)"""
#100Return true if string contains 'abc' not followed by '.'.
"""s= input()
count = 0
for i in s :
    if i == ".":
        count+=1
if count >= 1:
    print("false")
else:
    print("true")"""
#101Check if a string is a valid palindrome ignoring spaces and punctuation.
"""s = input()
nor = ""
for i in s.lower():
    if "a"<=i<="z":
        nor+=i
if nor == nor[::-1]:
    print("palindrome")
else:
    print("not")
print(nor)
"""
#99Check if a 'z' is happy (surrounded by same chars).
s = input()

for i in s:
    if i == "z":
        n = s.index(i)
        if s[n-1]=="z" and s[n+1]=="z" and s[n]=="z":
            print("happy")