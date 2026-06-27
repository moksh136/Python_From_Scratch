"""Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
"""

n = int(input("enter size"))
numbers = []
for i in range (n):
    x = int(input("enter element"))
    numbers.append(x)
print(numbers)
palindrome = []
count = 0
for i in numbers:
    temp = i
    rev = 0
    while i>0:
        d = i%10
        rev = rev*10 + d
        i = i//10
    if temp == rev:
        palindrome.append(temp)
        count += 1

print(sorted(palindrome))
print(palindrome)
print(count)
print(max(palindrome))
