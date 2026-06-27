"""
.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number"""
vehicle = input("Enter vehicle number: ")

if (
    len(vehicle) == 10 and
    vehicle[:2].isalpha() and
    vehicle[2:4].isdigit()
):
    print("Valid Vehicle Number")
else:
    print("Invalid Vehicle Number")