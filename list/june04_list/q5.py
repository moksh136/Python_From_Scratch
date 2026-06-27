"""
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers 
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input: 
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0"""
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter elements: ").split()))

positive = []
negative = []

for num in arr:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

result = []

i = 0
j = 0

while i < len(positive) and j < len(negative):
    result.append(positive[i])
    result.append(negative[j])
    i += 1
    j += 1

while i < len(positive):
    result.append(positive[i])
    i += 1

while j < len(negative):
    result.append(negative[j])
    j += 1

print("Rearranged Array:")
for num in result:
    print(num, end=" ")