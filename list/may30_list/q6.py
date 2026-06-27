"""5. Equilibrium Index Finder
===========================
Scenario
Find an index where:
# Sum of elements on the left side
Sum of elements on the right side
Requirements
* Read N and list elements from user
* Find equilibrium index
* If not found, display message
Test Case 1
Input:
[1, 3, 5, 2, 2]
Output:
Equilibrium Index = 2
Explanation:
1 + 3 = 2 + 2
Test Case 2
Input:
[1, 2, 3]
Output:
No Equilibrium Index Found"""
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
found = False
for i in range(n):
    before = 0
    right = 0
    for j in range(i):
        before += arr[j]
    for j in range (i+1, n):
        right += arr[j]

    if before == right:
        print("equilibrium fount", i)
        found = True
if found == False:
    print("no equilibrium index")