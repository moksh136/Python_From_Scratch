"""
 Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop"""
s = input("enter message:")
a = s.split()
for i in range (0 , len(a)):
    s = a[i]
    rev = ""
    i = len(s)-1
    while i >= 0:
        rev = rev + s[i]
        i-=1
    print(rev, end = " ")