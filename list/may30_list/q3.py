"""10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found"""
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
has = []
non = []
repeting = True
for i in arr:
    if i not in has or i not in non:
        count = 0
        for j in range(len(arr)):
            if i == arr[j] :
                count+=1
        if count>1:
            repeting = True
            non.append(i)
        else:
            repeting = False
            has.append(i)
res = []
for i in non:
    if i not in res:
        res.append(i)
if repeting:
    print("yea", res)
else:
    print("no")


    
