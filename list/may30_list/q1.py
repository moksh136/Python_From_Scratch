"""1. First Non-Repeating Number
Scenario
An online voting system stores vote IDs in a list.
Find the first vote ID that appears only once.
Requirements
* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message
Test Case 1
Input:
[4, 5, 1, 2, 1, 2, 4]
Output:
First Non-Repeating Number = 5
Test Case 2
Input:
[7, 7, 8, 8]
Output:
No Non-Repeating Number Found
"""
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
        if count==1:
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
