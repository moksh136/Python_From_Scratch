"""# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime Numbers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime Number: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime Numbers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime Number: Not Available
Prime List: []
Sorted Prime List: []

---

# Test Case 5

## Input

[29, 31, 37, 41]

## Expected Output

Prime Numbers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime Number: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41]

---
"""
n = int(input("enter size"))
numbers = []
prime_num=[]
non_prime =[]
count_prime_num=0
count_non_prime=0
for i in range (n):
    x = int(input("enter element"))
    numbers.append(x)
    count_prime =0
    for j in (2,x//2+1):
        if x%j==0:
            count_prime +=1
            
        
    if count_prime ==0:
        prime_num.append(x)
        count_prime_num += 1 
    else:
        non_prime.append(x)
        count_non_prime +=1


print(numbers)
print(prime_num)
print(count_prime_num)
print(non_prime)
print(count_non_prime)







"""


prime = []
prime_nu = ""
for i in numbers:
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        prime.append(i)
        prime_nu = prime_nu + i
print(prime)
print(prime_nu)

"""