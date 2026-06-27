#zbd435 -> bdz345
"""s = input("enter the string")
s1 = ""
s2 = ""
res = ""
for x in s :
    if x.isalpha():
        s1 = s1+x
    else:
        s2=s2+x

for x in sorted(s1):
    res+=x
for x in sorted(s2):
    res+=x
print(res)"""
#-------------------------
#a3b4->aaabbbb, ab2 = abab
"""s = input()
prev = ""
res = ""
for ch in s:
    if ch.isalpha():
        res+=ch
        prev=ch
    else:
        res = res+prev*(int(ch)-1)

print(res)"""
#-------------
# a3bg -> adbg
"""s = input()
prev = ""
res = ""
for ch in s:
    if ch.isalpha():
        res+=ch
        prev=ch
    else:
        new = chr(ord(prev)+int(ch))
        res = res+new

print(res)
"""
#-----------------------
#wap to reverse a string
"""s = input()
rev = ""
i = len(s)-1
while i >= 0:
    rev = rev + s[i]
    i-=1
print(rev)"""
"""rev = s[::-1]
print(rev)"""
#-------------------------
#wap to reverse a sentence
"""s = input()
a = s.split()
rev = ""
i = len(a)-1
while i >= 0:
    rev = rev + a[i] + " "
    i-=1
print(rev)"""
"""rev = a[::-1]
print(" ".join(rev))"""
#------------------------
#wap to reverse each word 
"""s = input()
a = s.split()
for i in range (0 , len(a)):
    s = a[i]
    rev = ""
    i = len(s)-1
    while i >= 0:
        rev = rev + s[i]
        i-=1
    print(rev, end = " ")"""
"""
rev = s[::-1]
rev2=rev.split()
print(" ".join(rev2[::-1]))"""
#------------------------------------
#wap to each word without using split
"""s = input()
word = ""
i = 0
while i<len(s):
    if s[i]!=' ':
        word = s[i]+word
    else:
        print(word, end = " ")
        word = ""
    i+=1
print(word , end = " ")"""
#----------------------------------------------
#wap for reverse sentence and reverse each word
"""s = input()
words = s.split()
i = len(words)-1
while i>= 0:
    word = words[i]
    rev = ""
    j = len(word)-1
    while j >= 0:
        rev = rev+word[j]
        j = j-1
    print(rev,end = " ")
    i-=1"""
#(HW)in this program we want result should be updated in original string
#-----------------------------------------------------------------------  
#WAP to find first not repeated character in string
"""s = input()
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
    print("not found")"""
#---------------------------------------
#WAP to find shortest word in a sentence
"""s = input()
word = s.split()
short = word[0]
for i in range (1, len(word)):
    if len(word[i])<len(short):
        short = word[i]
print(short)"""
#---------------------------------------
#WAP to find no of unique char in string
"""s = input()
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
        f+=1
    i+=1
print("count of unique",f)"""
#-----------------------------------------------------------------------------------------------------------
#WAP to find occurence of a word in string means our program count how many times a word appears in a string
"""s = input()
word = input()
count = 0
i = 0
while i <= len(s)-len(word):
    j = 0
    match = 1
    while j < len(word):
        if s[i+j]!=word[j]:
            match = 0
            break
        j+=1
    if match == 1:
        count+=1
    i+=1
print("no of occurence:", count)"""
#-----------------------------------------------
#WAP to remove duplicate words from a string(HW)
n = input("input:")
i = 0
str1 = ""

while i < len(n):
    ch = n[i]

    if (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122) or (48 <= ord(ch) <= 57) or ch == " ":
        str1 = str1 + ch

    i = i + 1

print(str1)