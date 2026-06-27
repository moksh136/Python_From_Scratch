"""2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found"""
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
has = []
non = None
repeting = True
for i in arr:
    if i not in has:
        count = 0
        for j in range(len(arr)):
            if i == arr[j] :
                count+=1
        if count>1:
            repeting = True
            non = i
            break
        else:
            repeting = False
            has.append(i)
if repeting:
    print("yea", non)
else:
    print("no")
