"""1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3"""
print("enter the size of list")
n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
print(arr)
large = arr[0]
small = arr[0]
count = 0
for i in arr:
    if large<i:
        large = i
print("highest :", large)
for i in arr:
    if small>i:
        small = i
print("small :", small)
for i in arr:
    if i>75:
        count+=1
print("count :", count)