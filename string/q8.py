"""
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username"""
a = input("Enter username: ")
f = 1
if len(a) < 5 or len(a) > 12:
    f = 0
elif not (("a" <= a[0] <= "z") or ("A" <= a[0] <= "Z")):
    f = 0
else:
    for ch in a:
        if not (("a" <= ch <= "z") or("A" <= ch <= "Z") or("0" <= ch <= "9") or ch == "_"):
            f = 0
if f == 1:
    print("Valid Username")
else:
    print("Invalid Username")