"""6. Product Except Self
======================
Scenario
For every element, calculate the product of all other elements except itself.
Requirements
* Read N and list elements from user
* Create a new list containing products
* Display the result
Test Case 1
Input:
[1, 2, 3, 4]
Output:
[24, 12, 8, 6]
Test Case 2
Input:
[2, 3, 5]
Output:
[15, 10, 6]
---"""
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
prod = []
for i in range(n):
    pro = 1
    for j in range(n):
        if arr[i]!=arr[j]:
            pro*=arr[j]
    prod.append(pro)
print(prod)