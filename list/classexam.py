 #how to read value of a list from user
"""a = list(map(int,input("enter value:").split()))
print(a)"""
#taking fix no of inputs in a list
"""a = int(input("no of element"))
name = []
for i in range(a):
    x = input()
    name.append(x)
print(name)"""
#different type of data input
"""data = input().split()
print(data)
data[0]=int(data[0])
data[1]=float(data[1])
data[2]=str(data[2])
print(data)"""
#--------------------------------------
"""print("enter id and name and marks")
id,name,marks=input().split()
data=[int(id), name,float(marks)]
print(data)"""
#write a program to add elemrnt of list
"""print("enter the size of list")
n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
sum = 0
for i in arr:
    sum+=i
print(sum)"""
#-------------------------------------
"""print("enter the size of list")
n = int(input("enter size"))
arr = []
i=0
while i<n:
    x = int(input("enter element"))
    arr.append(x)
    i+=1
sum = 0
for i in arr:
    sum+=i
print(sum)"""
#--------------------------------------
#wap to add even index value
"""print("enter the size of list")
n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
sum = 0
for i in range(len(arr)):
    if i%2 == 0:
        sum = sum + arr[i]
print(sum)"""
#wap to add even element of list
"""print("enter the size of list")
n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
sum = 0
for i in arr:
    if i%2==0:
        sum+=i
print(sum)
"""
#wap to add odd element of list
"""print("enter the size of list")
n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
sum = 0
for i in arr:
    if i%2!=0:
        sum+=i
print(sum)"""
#WAP to find max element in an arr
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
large = arr[0]"""
"""for i in arr:
    if i>large:
        large = i"""
"""for i in range(len(arr)):
    if arr[i]>large:
        large = arr[i]
print(large)"""
#WAP to find min element
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
small = arr[0]
for i in arr:
    if small > i:
        small = i
print(small)"""
#WAP to remove duplicate element from a list
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
prev = []
for i in arr:
    if i not in prev:
        prev.append(i)
print(prev)"""
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
for i in arr:
    count = 0
    for j in arr:
        if i==j:
            count+=1
    if count>1:
        arr.remove(i)
print(arr)"""
#WAP tp find second largest in a list:
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
prev = []
for i in arr:
    if i not in prev:
        prev.append(i)
prev.sort()
print(prev[-2])"""
#WAP program to separate even sna odd number from a list
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
odd = []
even = []
for i in arr:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)"""
#WAP to find common element bw two list
"""n = int(input("enter size"))
arr1 = []
arr2 = []
for i in range (n):
    x = int(input("enter element"))
    arr1.append(x)
print(arr1)
for i in range (n):
    y = int(input("enter element"))
    arr2.append(y)
print(arr2)
res = []
for i in arr1:
    if i in arr2:
        res.append(i)
print(res)"""
#WAP to check no is greater than 10 and even
"""n = int(input("enter size"))
arr1 = []
arr2 = []
for i in range (n):
    x = int(input("enter element"))
    arr1.append(x)
print(arr1)
for i in range (n):
    y = int(input("enter element"))
    arr2.append(y)
print(arr2)
res = []
for i in arr1:
    if i in arr2 and i>=10 and i % 2 == 0:
        res.append(i)
print(res)"""
#WAP to merge two list without duplicate
"""a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
merge = a +b
res = []
for i in merge:
    if i not in res:
        res.append(i)
print(res)"""
#WAP to rev a list without built in function
"""a = [1, 2, 3, 4, 5]
res = []
for i in range(len(a)-1,-1,-1):
    res.append(a[i])
print(res)"""
#___________________________________
"""for i in a:
    res = [i] + res
print(res)"""
#WAP to move all 0 to end
"""a = [1, 2, 0, 4, 0 , 3, 0]
zero = []
nonzero = []
for i in a:
    if i == 0:
        zero.append(i)
    else:
        nonzero.append(i)
res = nonzero+zero
print(res)"""
#WAP for the  peak element 
# an element is called peak element if its value is not smaller than adjacent element if the exist
#WAP to find index of any one peak element
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
index = -1
for i in range(n):
    if i == 0:
        if n == 1 or arr[i]>=arr[i+1]:
            index = i
            break
    elif i == n-1:
        if arr[i]>=arr[i-1]:
            index = i
            break
    else:
        if arr[i]>= arr[i-1] and arr[i]>=arr[i+1]:
            index = i
            break
if index != -1:
    print(index, arr[index])
else:
    print("not found")"""
#WAP to find sum leaders in an arr
#an element is called a leader if it is greater than all  element /
# to its right side and right most element is aalways a leader
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
sum = 0
for i in range (len(arr)):
    isleader = True
    for j in range (i+1, len(arr)):
        if arr[i]<=arr[j]:
            isleader = False
            break
    if isleader:
        sum+=arr[i]
print(sum)"""
# given an unshorted array of size n having both -ve and +ve integer task is to place 
# all -ve element at the end of array without chnging order og +ve and-ve elements
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
neg = []
pos = []
for i in arr:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
res = pos+neg
print(res)"""
#WAP to cyclicly rotate arr by 1
"""n = int(input("enter size"))
arr = []
for i in range (n):
    x = int(input("enter element"))
    arr.append(x)
last = arr[n-1]
i = n-1
while i>0:
    arr[i] = arr[i-1]
    i = i-1
arr[0]= last
print(arr)"""
#list comprehension
"""a = [1,2,3,4,5]
b = [i for i in a if i%2 ==0 and i>3]
print(b)"""
"""a = [1,2,3,4,5]
b = ["even" if i%2 ==0 else "odd" for i in a]
print(b)"""

"""a = ["deepika", "virat", "rcb"]
b = [i for i in a if len(i)>3]
print(b)  """#['deepika', 'virat']

"""a = ["deepika", "virat", "rcb"]
b = [i.upper() for i in a]
print(b)"""  #['DEEPIKA', 'VIRAT', 'RCB']

"""a = [11, 2, 5, 2, 8]
b = [i*10 if i%2==0 else i for i in a]
print(b)"""#[11, 20, 5, 20, 80]

#nested list
"""a = [1, 2, [1, 3], 5]
print(a)
print(a[2])
print(a[2][1])"""
"""a = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]"""
"""print(a[0])
print(a[1])
print(a[2])"""
"""for i in a:
    print()
    for j in i:
        print(j, end = " ")"""
"""for i in range(len(a)):
    print()
    for j in range (len(a[i])):
        print(a[i][j], end = " ")"""

"""a = [
    [10, "deep"],
    [10, 20 , 30],
    [70],
    ["abc", "xyz"]
]
for i in range(len(a)):
    print()
    for j in range (len(a[i])):
        print(a[i][j], end = " ")"""
#updating nested list element 
#====================================================================================
#WAP to read rows and columns from user read all the element from user and display them 
"""row = int(input())
col = int(input())
matrix = []
for i in range (row):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print(matrix)
print("elements are")
for i in matrix:
    for j in i:
        print(j, end = " ")
    print()"""
#wap to display sum of all matrix element
"""row = int(input("enter rows:"))
col = int(input("enter columns:"))
matrix = []
for i in range (row):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
sum = 0
print("elements are")
for i in matrix:
    for j in i:
        sum+=j
i = 0
while i<len(row):
    j = 0
    while j<len(col):
        sum+=j
        j+=1
    i+=1
print(sum)
"""
#WAP to find sum of diagonal element
"""row = int(input("enter rows:"))
col = int(input("enter columns:"))
matrix = []
for i in range (row):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
sum = 0
for i in range(len(matrix)):
    sum+=matrix[i][i]
print(sum)"""
#WAP to sum of odd number in mat
"""row = int(input("enter rows:"))
col = int(input("enter columns:"))
matrix = []
for i in range (row):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print(matrix)
sum = 0
for i in matrix:
    for j in i:
        if j%2!=0:
            sum+=j
print(sum)"""
#WAP to search element in matrix
"""row = int(input("enter rows:"))
col = int(input("enter columns:"))
tofind = int(input("enter element to search"))
matrix = []
for i in range (row):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print(matrix)
found = False
for i in matrix:
    for j in i:
        if j == tofind:
            print("found")
            found = True
            break
if found == False:
    print("not found")"""
#--------------------------------------------------------
"""row = int(input("enter rows:"))
col = int(input("enter columns:"))
tofind = int(input("enter element to search"))
matrix = []
for i in range (row):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print(matrix)
found = False
for i in range (len(matrix)):
    for j in range(len(matrix(i))):
        if matrix[i][j] == tofind:
            print("found", i , j)
            found = True
            break
if found == False:
    print("not found")"""
#WAP to reverse each row
row = int(input("enter rows:"))
col = int(input("enter columns:"))
matrix = []
for i in range (row):
    rows = []
    for j in range(col):
        rows.append(int(input()))
    matrix.append(rows)
print(matrix)

for i in matrix:
    i.reverse()
"""for row in matrix:
    i =0
    j =len(row)-1
    while i<j:
        t = row[i]
        row[i] = row [j]
        row [j]= t
        i+=1
        j-=1 """
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end = " ")
    print()
    
#WAP to add two matrix
"""rows = int(input("enter rows:"))
col = int(input("enter columns:"))
a = []
print("for mat 1")
for i in range (rows):
    row = []
    for j in range(col):
        row.append(int(input()))
    a.append(row)
print("for mat 2")
b = []
for i in range (rows):
    row = []
    for j in range(col):
        row.append(int(input()))
    b.append(row)
mat = []
for i in range(rows):
    sum = []
    for j in range(col):
        sum.append(a[i][j]+b[i][j])
    mat.append(sum)
print(mat) 
for i in mat:
    for j in i:
        print(j, end =" ")
    print()"""
#WAP to multiply two matrix
"""r1 = int(input("enter rows:"))
c1  = int(input("enter columns:"))
a = []
print("for mat 1")
for i in range (r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    a.append(row)
print("for mat 2")
r2= int(input("enter rows:"))
c2 = int(input("enter columns:"))
b = []
for i in range (r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    b.append(row)
if c1!=r2:
    print("multiplication not possible")
else:
    res = []
    for i in range (r1):
        row = []
        for j in range (c2):
            row.append(0)
        res.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j ] = res[i][j] + a[i][k] * b[k][j]
    
    for i in range (r1):
        for j in range(c1):
            print(a[i][j], end = " ")
        print()

    for i in range (r2):
        for j in range(c2):
            print(b[i][j], end = " ")
        print()
    
    for i in res:
    
        print(i)
"""
#WAP to read 3d array element from user and display them
#given an array of n integer and an integer k find the no of pairs  of element in the arr 
#/whose sum is equal to k
"""n = [1, 1, 1, 1]
k = 2
count = 0
for i in range (len(n)):
    for j in range(i+1, (len(n))):
        if n[i]+n[j] == k:
            count+=1
print(count)"""
#WAP to count unique word in string using set
"""s = input()
word = s.split()
u = set(word)
print(u)"""
#WAP to check unique char in a string
"""str = input()
print(set(str))
if len(str)==len(set(str)):
    print("no duplicate")
else:
    print("found")"""
#WAP to find first non repeting char using set
t = (1, 2, 3, 4)
t[1] = 4
print(t)