"""Second Largest Unique Number
Scenario

A sports academy stores athlete scores in a list.

Find the second largest unique score.

Requirements
Read N and list elements from user
Find second largest unique number
If not available, display a message
Test Case

Input:

[10, 20, 30, 40, 40]

Output:

Second Largest = 30"""
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
sort = sorted(arr)
lar = []
for i in sort:
    if i not in lar:
        lar.append(i)
print(lar[-2])