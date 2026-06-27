"""4.
Assignment: Scholarship Eligibility System (Using filter(), map(), and sorted() with Lambda Expressions)

A university is offering scholarships to students based on their academic performance.

The scholarship committee has decided on the following rules:

Only students who score 75 marks or above are eligible for the scholarship.
Eligible students will receive 5 bonus marks to reward their outstanding performance.
Finally, the updated marks should be displayed in descending order.

As a software developer, your task is to automate this process using Python.

Note: Use filter() to select eligible students, map() to add the bonus marks, and sorted() to display the final marks in descending order. All three operations must use lambda expressions.

Task

Write a Python program that:

Filters students who have scored 75 or above.
Adds 5 bonus marks to each eligible student.
Sorts the updated marks in descending order.
Displays the final list of scholarship marks.
Input Format
The first line contains an integer N, representing the number of students.
The second line contains N space-separated marks.
Output Format

Display the updated scholarship marks in descending order.

Sample Input
Enter the number of students:
8

Enter the marks:
65 80 92 74 88 76 55 95
Sample Output
Scholarship Marks:
100 97 93 85 81
"""
n = int(input("Enter the number of students: "))

marks = list(map(int, input("Enter the marks: ").split()))

eligible = filter(lambda x: x >= 75, marks)

bonus = map(lambda x: x + 5, eligible)

result = sorted(bonus, reverse=True)

print("Scholarship Marks:")
print(*result)
"""
recursion:
Assignment 1: Smart Street Lights (Fibonacci Series)

A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

Month 1 → 0 lights
Month 2 → 1 light
Every following month, the number of lights installed is the sum of the previous two months.

As a software developer, your task is to help the city planning department generate the installation schedule.

Task

Write a recursive function to print the first N Fibonacci numbers.

Input
Enter the number of months:
7
Output
0 1 1 2 3 5 8"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter the number of months: "))

for i in range(n):
    print(fibonacci(i), end=" ")

"""
Assignment 2: Binary Converter for Embedded System

An embedded systems company develops microcontrollers that understand only binary values. Engineers enter decimal numbers, and the software must convert them into binary before sending them to the device.

As a software developer, write a recursive program to perform this conversion.

Task

Write a recursive function to convert a decimal number into its binary representation.

Input
Enter a decimal number:
25
Output
Binary Number = 11001

Note: Do not use Python's built-in bin() function.
"""
def binary(n):
    if n == 0:
        return
    binary(n // 2)
    print(n % 2, end="")

num = int(input("Enter a decimal number: "))

print("Binary Number =", end=" ")

if num == 0:
    print(0)
else:
    binary(num)
"""

Assignment 3: Security PIN Verification (Palindrome Number)

A bank allows customers to choose a special PIN. For promotional purposes, the bank rewards customers whose PIN is a palindrome (reads the same from left to right and right to left).

As a software developer, write a recursive program to verify whether the entered PIN is a palindrome.

Task

Write a recursive function to reverse the given number and determine whether it is a palindrome.

Input 1
Enter PIN:
1221
Output 1
Palindrome Number
Input 2
Enter PIN:
1234
Output 2
Not a Palindrome Number
"""
def reverse(num, rev=0):
    if num == 0:
        return rev
    return reverse(num // 10, rev * 10 + num % 10)

num = int(input("Enter PIN: "))

if num == reverse(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
"""
Assignment 4:
 Lottery Ticket Verification (Count Occurrences Using Recursion)

A lottery company assigns a unique ticket number to every participant. Before announcing the results, the company wants to determine how many times a lucky digit appears in a ticket number. This helps identify tickets eligible for special bonus rewards.

As a software developer, your task is to write a recursive Python program that counts the number of times a given digit appears in the ticket number.

Task

Write a recursive function to count the occurrences of a given digit in a ticket number.

Input Format
The first line contains an integer representing the Ticket Number.
The second line contains an integer representing the Lucky Digit.
Output Format

Display the number of times the lucky digit appears in the ticket number using the format:

Digit <Lucky Digit> appears <Count> times.
Sample Input
Enter Ticket Number:
1122334412

Enter Lucky Digit:
2
Sample Output
Digit 2 appears 3 times.
Sample Input 2
Enter Ticket Number:
987654321

Enter Lucky Digit:
5
Sample Output 2
Digit 5 appears 1 time.
Sample Input 3
Enter Ticket Number:
11111111

Enter Lucky Digit: 
2
Sample Output 3
Digit 2 appears 0 times."""
def count_digit(number, digit):
    if number == 0:
        return 0

    if number % 10 == digit:
        return 1 + count_digit(number // 10, digit)
    else:
        return count_digit(number // 10, digit)

ticket = int(input("Enter Ticket Number: "))
lucky = int(input("Enter Lucky Digit: "))

count = count_digit(ticket, lucky)

if count == 1:
    print(f"Digit {lucky} appears {count} time.")
else:
    print(f"Digit {lucky} appears {count} times.")