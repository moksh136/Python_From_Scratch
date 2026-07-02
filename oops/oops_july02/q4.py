"""Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage	Grade
90 and above	A
75 to 89	B
60 to 74	C
Below 60	D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B"""

class Student:
    def __init__(self , roll_number, student_name, mark1, mark2, mark3):
        self.roll_number = roll_number
        self.student_name = student_name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def calculate(self):
        self.total = self.mark1 + self.mark2 + self.mark3
        self.percentage = self.total / 3
        if self.percentage >= 90:
            self.grade = "A"
        elif self.percentage >= 75 and self.percentage<90:
            self.grade = "B"
        elif self.percentage >= 60 and self.percentage<75:
            self.grade = "C"
        else:
            self.grade = "D"
    def display(self):
        print("------ Student Result ------")
        print("Roll Number:", self.roll_number)
        print("Student name:", self.student_name)
        print("Total Marks:", self.total)
        print("percentage :", self.percentage)
        print("Grade :", self.grade)
roll = input("enter roll number:")
name = input("enter student's name:")
m1 = int(input("enter marks 1:"))
m2 = int(input("enter marks 2:"))
m3 = int(input("enter marks 3:"))
s1 = Student(roll, name, m1, m2, m3)
s1.calculate()
s1.display()