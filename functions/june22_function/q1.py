"""1.
Employee Record Sorting (Lambda)


A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

Task

Write a Python program to sort the employee records using a lambda expression.

Input
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]"""
emp = []

n = int(input("Enter the number of employees: "))

for i in range(n):
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    emp.append((name, salary))

emp.sort(key=lambda x: x[1])

print(emp)