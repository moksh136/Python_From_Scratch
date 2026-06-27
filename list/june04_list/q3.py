""".

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45"""
rows = int(input("Enter number of employees: "))
cols = int(input("Enter number of months: "))

matrix = []

print("Enter performance scores:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

while True:
    print("\nMENU")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        max_total = sum(matrix[0])
        emp_no = 1

        for i in range(rows):
            total = sum(matrix[i])

            if total > max_total:
                max_total = total
                emp_no = i + 1

        print(f"Employee {emp_no} has Highest Total Score = {max_total}")

    elif choice == 2:
        min_avg = None
        month_no = 0

        for j in range(cols):
            total = 0

            for i in range(rows):
                total += matrix[i][j]

            avg = total / rows
            print(f"Month {j+1} Average = {avg}")

            if min_avg is None or avg < min_avg:
                min_avg = avg
                month_no = j + 1

        print(f"Month {month_no} has Lowest Average Score = {min_avg}")

    elif choice == 3:
        for i in range(rows):
            max_score = matrix[i][0]

            for j in range(cols):
                if matrix[i][j] > max_score:
                    max_score = matrix[i][j]

            print(f"Employee {i+1} Max Score = {max_score}")

    elif choice == 4:
        print("Thank You for Using Matrix Performance Evaluation System")
        break

    else:
        print("Invalid Choice")