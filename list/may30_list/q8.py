"""7. Array Rotation Analyzer
==========================
Scenario
Rotate the array K times towards the right.
Requirements
* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array
Test Case 1
Input:
Array = [1, 2, 3, 4, 5]
K = 2
Output:
[4, 5, 1, 2, 3]
Test Case 2
Input:
Array = [10, 20, 30, 40]
K = 1
Output:
[40, 10, 20, 30]
---
"""
n = int(input("Enter size: "))
k = int(input("Enter K: "))

arr = []

for i in range(n):
    arr.append(int(input()))

k = k % n

start = []
last = []

for i in range(0, n - k):
    start.append(arr[i])

for i in range(n - k, n):
    last.append(arr[i])

res = last + start

print("Rotated Array =", res)
