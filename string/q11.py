"""Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID"""
emp = input("Enter Employee ID: ")
f = 1
if len(emp) != 8:
    f = 0
elif emp[0] != "E" or emp[1] != "M" or emp[2] != "P":
    f = 0
else:
    for ch in emp[3:]:
        if not ("0" <= ch <= "9"):
            f = 0
if f == 1:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")