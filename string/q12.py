"""
Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
"""
a = input("Enter first product code: ")
b = input("Enter second product code: ")
a = a.replace(" ", "").lower()
b = b.replace(" ", "").lower()
a = sorted(a)
b = sorted(b) 
if a == b:
    print("Both Product Codes are Matching")
else:
    print("Product Codes are Not Matching")