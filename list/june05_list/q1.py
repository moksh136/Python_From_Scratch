"""=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000"""
n = int(input("Enter number of employees: "))

employees = []

for i in range(n):
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employees.append([emp_id, emp_name, department, salary])

print("\nAll Employee Details:")
for emp in employees:
    print(emp[0], emp[1], emp[2], emp[3])

# Highest Salary Employee
highest = employees[0]

for emp in employees:
    if emp[3] > highest[3]:
        highest = emp

print("\nHighest Salary Employee:")
print(highest[0], highest[1], highest[2], highest[3])

# Lowest Salary Employee
lowest = employees[0]

for emp in employees:
    if emp[3] < lowest[3]:
        lowest = emp

print("\nLowest Salary Employee:")
print(lowest[0], lowest[1], lowest[2], lowest[3])

# Average Salary
total = 0

for emp in employees:
    total += emp[3]

average = total / n

print("\nAverage Salary:")
print(average)

# Department-wise Employees
dept = input("\nEnter department: ")

print(f"\nEmployees in {dept} Department:")

for emp in employees:
    if emp[2].lower() == dept.lower():
        print(emp[0], emp[1], emp[2], emp[3])