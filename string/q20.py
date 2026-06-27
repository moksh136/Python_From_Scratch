"""
Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowercase - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found
"""
s = input("enter the string")
s1 = ""
s2 = ""
res = ""
digit = 0
for x in s :
    if x.isalpha():
        if "A"<=x<="Z":
            cap = chr((ord(x))+32)
            s1 = s1+cap
        else:
            s1+=x
    else:
        if "0"<=x<="9":
            s2=s2+x
            digit = 1
for x in sorted(set(s1)):
    res+=x
for x in sorted(s2,reverse=True):
    res+=x
if digit == 0:
    print(res, "no digit found")
else:
    print(res)