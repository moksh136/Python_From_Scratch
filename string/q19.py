"""
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website"""
s = input("enter website:")
l = len(s)
if (s[0]=="w"and s[1]=="w" and s[2]=="w") and (s[l-4]=="." and s[l-3]=="c"and s[l-2]=="o" and s[l-1]=="m"):
    print("valid website")
else:
    print("invalid website")
"""
s = input("Enter website: ")

if s.startswith("www") and s.endswith(".com"):
    print("Valid Website")
else:
    print("Invalid Website")"""