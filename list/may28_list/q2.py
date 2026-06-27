""".Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []"""
n = int(input("enter size"))
salary = []
for i in range (n):
    x = int(input("enter element"))
    salary.append(x)
print(salary)
sum = 0
for i in salary:
    sum += i
avg = sum / n
print("average =", avg)
for i in salary:
    if i > avg:
        print("above average =", i)