"""
3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.
7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"
---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------
Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit
Enter your choice: 1
Enter rows: 3
Enter columns: 3
Enter matrix elements:
153 121 10
370 22 44
407 15 131
Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1
---------------------------------------------------------
Enter your choice: 2
Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2
========================================================="""
def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


def is_palindrome(num):
    return str(num) == str(num)[::-1]


rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

while True:
    print("\nMENU")
    print("1. Count Armstrong Numbers Row-wise")
    print("2. Count Palindrome Numbers Column-wise")
    print("3. Display Average of Each Row")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for i in range(rows):
            count = 0
            for j in range(cols):
                if is_armstrong(matrix[i][j]):
                    count += 1
            print(f"Row {i+1} Armstrong Count = {count}")

    elif choice == 2:
        for j in range(cols):
            count = 0
            for i in range(rows):
                if is_palindrome(matrix[i][j]):
                    count += 1
            print(f"Column {j+1} Palindrome Count = {count}")

    elif choice == 3:
        for i in range(rows):
            avg = sum(matrix[i]) / cols
            print(f"Row {i+1} Average = {avg:.2f}")

    elif choice == 4:
        print("Thank You for Using Matrix Quality Check System")
        break

    else:
        print("Invalid Choice")