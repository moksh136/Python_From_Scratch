"""
Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012"""
n = input()
a = len(n)
for i in range (1, (a-4)+1):
    print("*", end= "")
for i in range (a-4, a):
    print(n[i], end = "")