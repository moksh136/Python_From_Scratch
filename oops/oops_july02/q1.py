"""Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0"""

class Employee:
    def __init__(self, employee_id, employee_name, basic_salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.basic_salary = basic_salary
    def calculate(self):
        self.hra = self.basic_salary*0.2
        self.da = self.basic_salary*0.15
        self.gross_salary = self.basic_salary + self.hra + self.da
    def display(self):
        print("------ Employee Salary Details ------")
        print("Employee name :", self.employee_name)
        print("Employee id :", self.employee_id)
        print("Basic Salary :", self.basic_salary)
        print("HRA:", self.hra)
        print("DA :", self.da)
        print("Gross Salary:", self.gross_salary)

id = input("enter id:")
name = input("enter name:")
sal = int(input("emter salary:"))
s1 = Employee(id, name, sal)
s1.calculate()
s1.display()
  