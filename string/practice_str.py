#1Find the length of a string
"""s = input()
count = 0 
for ch in s:
    count+=1
print(count)"""
#2Copy one string to another
"""s1 = input()
s2 = ""
for ch in s1:
    s2+=ch
print(s2)"""
#3Concatenate two strings.
"""s1 = input()
s2 = input()
print(s1+" "+s2)"""
#Compare two strings (case-sensitive).
"""s1 = input()
s2 = input()
if s1 == s2:
    print("equal")
else:
    print("not equal")"""
#Compare two strings ignoring case
"""s1 = input()
s2 = input()
r1=""
r2=""
for ch in s1:
    if "A"<=ch<="Z":
        let = ord(ch)+32
        r1= r1 + chr(let)
    else:
        r1+=ch
for ch in s2:
    if "A"<=ch<="Z":
        let = ord(ch)+32
        r2= r2 + chr(let)
    else:
        r2+=ch
if r1 == r2:
    print("equal")
else:
    print("not equal")"""
#Convert a string to uppercase
"""s = input()
res = ""
for ch in s:
    if "a"<=ch<="z":
        let = ord(ch)-32
        res = res +chr(let)
    else:
        res+=ch
print(res)"""
#Convert a string to lowercase.
"""s = input()
res = ""
for ch in s:
    if "A"<=ch<="Z":
        let = ord(ch)+32
        res = res +chr(let)
    else:
        res+=ch
print(res)"""
#Toggle the case of each character
"""s = input()
res = ""
for ch in s:
    if "A"<=ch<="Z":
        let = ord(ch)+32
        res = res +chr(let)
    elif "a"<=ch<="z":
        let = ord(ch)-32
        res = res +chr(let)
print(res)"""
#Check whether a string is empty.
"""s = input()
if s == "":
    print("true")
else:
    print("false")"""
#Trim leading, trailing, or extra spaces
"""s = input()
words = s.split()
res = ""
for ch in words:
    res= res + ch + " "
print(res)"""
#Get the character at a given index.
"""s = input()
n = int(input())
print(s[n])"""
#Get the Unicode code point of a character at index.
"""s = input()
n = int(input())
print(ord(s[n]))"""
#3Get the Unicode code point before index
"""s = input()
n = int(input())
print(ord(s[n-1]))"""
#Find the first occurrence of a character.
"""s = input()
char = input()
for i in range(len(s)):
    if s[i]==char:
        print(i)
        break"""
#Find the last occurrence of a character.
"""s = input()
char = input()
for i in range(len(s)-1,-1,-1):
    if s[i]==char:
        print(i)
        break"""
#Count total occurrences of a character.
"""s = input()
char = input()
count = 0
for i in range(len(s)-1,-1,-1):
    if s[i]==char:
        count+=1
print(count)"""
#Remove occurrences of a character.
"""s = input()
char = input()
res = ""
for i in range(len(s)):
    if s[i]!=char:
        res+=s[i]
        
print(res)"""
#Replace occurrences of a character.
"""s = input()
char = input()
res = ""
for i in range(len(s)):
    if s[i]==char:
        res+="x"
    else:
        res+=s[i]
print(res)"""
#Find the highest frequency character.
"""s = input()
max_count = 0
max_char = ""
for ch in s:
    count = 0
    for c in s:
        if ch == c:
            count += 1
    if count>max_count:
        max_count= count
        max_char = ch

print(max_char)"""
#Find the lowest frequency character.
"""s = input()
low_count = len(s)
low_char = ""
for ch in s:
    count = 0
    for c in s:
        if ch == c:
            count += 1
    if count < low_count:
        low_count = count
        low_char = ch
print(low_char)"""
#Find the first non-repeating character.
"""s = input()
for ch in s :
    count = 0
    for c in s:
        if ch == c:
            count+=1
    if count == 1:
        print(ch)
        break"""
#Find the last repeating character
"""s =input()

for i in range(len(s)-1, -1, -1):
    count = 0
    
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    
    if count > 1:
        print(s[i])
        break"""
#Print all characters that occur exactly twice
"""s = input()
printed = ""
for ch in s:
    count = 0 
    for c in s :
        if ch == c:
            count += 1
    if count == 2 and ch not in printed:
        print(ch)
        printed+=ch"""
#Check if all characters in a string are unique
"""s = input()
f = 0
for ch in s:
    count = 0
    for c in s:
        if ch == c:
            count += 1
    if count == 1:
        f = 1
    else:
        f = 0

if f == 1:
    print("True")
else:
    print("False")"""
#Count total words in a string.
"""s = input()
word = s.split()
print(len(word))"""
#Find the first occurrence of a word.
"""text = input("Enter sentence: ")
word = input("Enter word to search: ")
pos = -1
for i in range(len(text) - len(word) + 1):
    match = True
    for j in range(len(word)):
        if text[i + j] != word[j]:
            match = False
            break
    if match:
        pos = i
        break
print(pos)"""
#Find the last occurrence of a word.
"""text = input("Enter sentence: ")
word = input("Enter word to search: ")
pos = -1
for i in range(len(text) - len(word) + 1):
    match = True
    for j in range(len(word)):
        if text[i + j] != word[j]:
            match = False
            break
    if match:
        pos = i
print(pos)"""
#Count occurrences of a word.
"""text = input("Enter sentence: ")
word = input("Enter word to search: ")
words = text.split()
count = 0
for ch in words:
    if ch == word:
        count+=1
print(count)
"""
#Remove occurrences of a word.
"""text = input("Enter sentence: ")
word = input("Enter word to search: ")
words = text.split()
res = ""
for ch in words:
    if ch != word:
        res = res + ch + " "
print(res)"""
#Replace a word with another word.
"""s = input()
old = input()
new = input()
res = ""
i = 0
while i < (len(s)):
    match = True
    if i + len(old) <= len(s):
        for j in range(len(old)):
            if s[i+j]!=old[j]:
                match= False
                break
        if match:
            res+=new
            i+=len(old)
        else:
            res+=s[i]
            i+=1

    else:
        res+=s[i]
        i+=1
print(res)"""
#Remove duplicate words.
"""s = input()
words = s.split()
res =""
for ch in words:
    if ch not in res:
        res = res + ch + " "

print(res)"""
#Count frequency of each word.
"""s = input()
words = s.split()
prev = ""
for ch in words:
    if ch not in prev:
        count = 0
        for i in range(len(words)):
            if words[i]==ch:
                count +=1
        print(ch , count)
        prev= prev + ch + " "
        """
#Find the longest word.
"""s = input()
words = s.split()
longest = ""
for ch in words:
    if len(ch) > len(longest):
        longest = ch
print(longest)"""
#Find the shortest word
"""s = input()
words = s.split()
short = words[0]
for ch in words:
    if len(ch) < len(short):
        short = ch
print(short)"""
#Find the first palindrome word
"""s = input()
words = s.split()
for ch in words:
    original = ch
    rev = ""
    for i in range (len(ch)-1,-1,-1):
        rev = rev + ch[i]
    if original==rev:
        print(original)"""
#Reverse order of words.
"""s = input()
words = s.split()
res = ""
for i in range(len(words)-1,-1,-1):
    res = res + words[i] + " "

print(res)

"""
#Reverse each word.
"""s = input()
words = s.split()
res= ""
for ch in words:
    rev = ""
    for i in range(len(ch)-1,-1,-1):
        rev+=ch[i]
    res =res + rev + " "
print(res)"""
#Reverse words without split()
"""s = input()
res = ""
for i in range (len(s)-1, -1, -1):
    res = res + s[i]
print(res)"""
#Search all occurrences of a character.
"""s = input()
char = input()
for i in range (len(s)):
    if s[i]==char:
        print(i)"""
#Search all occurrences of a word.
"""s = input()
word = input()
words = s.split()
count = 0
for ch in words :
    if word == ch:
        count +=1

print(count)"""
#Check if a string contains a substring (without using built-in method)
"""s1= input()
s2 = input()
count = 0
for i in range(len(s1)-len(s)):
    for j in range(len(s2)):
        if s1[i+j]!= s2[j]:
            break
        else:
            count+=1
if count == len(s2):
    print("found")
else:
    print("not found")"""
#42 Check if two strings are equal without equals()
"""s1= input()
s2 = input()
count = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i+j]!= s2[j]:
            break
        else:
            count+=1
if count == len(s2):
    print("equal")
else:
    print("not equal")"""
#43Check if two strings are rotations of each other.
"""s1 = input()
s2 = input()
if len(s1) == len(s2):
    if s2 in s1+s1:
        print("True")
else:
    print("false")"""
#44 Check if two strings are anagrams.
"""s1 = input()
s2 = input()
if len(s1) == len(s2):
    count= 0 
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count+=1
    if len(s1)== count:
        print("anagrams")
    else:
        print("not anagram")
else:
    print("not anagram")"""
#45 Check whether a string starts with or ends with another string
"""s = input()
words = s.split()
prefix = input()
suffix = input()
if words[0]==prefix:
    print("true")
else:
    print("false")
if words[len(words)-1] == suffix:
    print("true")
else:
    print("false")"""
#46Check if a substring appears at both the start and end.
"""s1 = input()
s2 = input()
start = True
end = True
n = len(s2)
for i in range (n):
    if s1[i] != s2[i]:
        start = False
j = len(s1)-n
for i in range (n):
    if s1[j+i]!= s2[i]:
        end = False
if start and end:
    print("true")
else:
    print("false")
"""
#47Check if one string is a substring of another using only concatenation.
"""s1 = input()
s2 = input()
s = s2+s2
if s1 in s:
    print("true")
else:
    print("false")"""
#48 Remove all vowels.
"""s = input()
res = ""
for ch in s:
    if ch not in "aeiou" and "AEIOU":
        res+=ch
print(res)
"""
#49Replace all consonants with ''
"""s = input()
res =""
for ch in s:
    if ch in "aeiou" and "AEIOU":
        res+=ch
    else:
        res+="'"
print(res)"""
#54Replace all duplicate characters with '$'.
"""s = input()
res = ""
for ch in s:
    if ch not in res:
        res+=ch
    else:
        res+="$"

print(res)"""
#55 Reverse only vowels.
"""s = input()
v = ""
res = ""
for ch in s:
    if ch in "AEIOUaeiou":
        v = ch + v
j = 0
for ch in s:
    if ch not in v:
        res+=ch
    else:
        res+=v[j]
        j+=1
print(res)"""
#57Merge two strings alternatively (char by char).
"""s1 = input()
s2 = input()
res = ""
for i in range(len(s1)):
    res = res + s1[i] + s2[i]
print(res)"""
#61Count total alphabets, digits, and special characters.
"""s = input()
alpha = 0
digit = 0
special = 0
for ch in s:
    if ch.isalpha():
        alpha+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
print("alphabet :", alpha)
print("digit :", digit)
print("special char :", special)"""
#63Count frequency of each character.
"""s = input()
prev = ""
for ch in s:
    if ch not in prev:
        count =0
        for i in range(len(s)):
            if s[i]==ch:
                count+=1
        print(ch, count)
    prev+=ch"""
#66Count number of sentences in a paragraph.
"""s = input()
count = 0
for ch in s:
    if ch == ".":
        count+=1
print("no of sentence:", count)
"""
#71Print all substrings.
s = input()
for i in range (len(s)):
    j = 0
    while j <= len(s):
        print(s[i], end = " ")
        j+=1
