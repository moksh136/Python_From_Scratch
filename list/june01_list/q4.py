"""
====================================================================
 Warehouse Inventory Multiplication Analyzer
====================================================================


A warehouse stores product quantities in different sections and racks.
The inventory data is maintained in the form of a matrix.

Rows represent warehouse sections.
Columns represent racks.
Each cell contains the quantity of products stored.

The warehouse manager wants to display the inventory matrix and find
the multiplication of all quantities stored in the warehouse.

Requirements

* Read number of rows from user
* Read number of columns from user
* Read all matrix elements from user
* Display the complete matrix
* Find multiplication of all elements
* Display the final product

Test Case 1

Input:

Rows = 2
Columns = 3

Matrix:

1 2 3
4 5 6

Output:

Matrix:

1 2 3
4 5 6

Multiplication of All Elements = 720

------------------------------------------------------------

Test Case 2

Input:

Rows = 3
Columns = 2

Matrix:

2 3
4 5
1 2

Output:

Matrix:

2 3
4 5
1 2

Multiplication of All Elements = 240

------------------------------------------------------------

Test Case 3

Input:

Rows = 2
Columns = 2

Matrix:

10 2
3 1

Output:

Matrix:

10 2
3 1

Multiplication of All Elements = 60

------------------------------------------------------------

Test Case 4

Input:

Rows = 2
Columns = 2

Matrix:

0 2
3 4

Output:

Matrix:

0 2
3 4

Multiplication of All Elements = 0

------------------------------------------------------------

Additional Requirements

Also display:

Total Number of Elements
Largest Element
Smallest Element
Multiplication of All Elements

Sample Output

===== MATRIX REPORT =====

Matrix:

1 2 3
4 5 6

Total Elements            : 6
Largest Element           : 6
Smallest Element          : 1
Multiplication of Elements: 720"""
row = int(input("enter no of rows:"))
col = int(input("enter no of columns:"))
matrix = []
for i in range(row):
    row = []
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
largest = matrix[0][0]
smallest = matrix[0][0]
for i in matrix:
    for j in i:
        if j>largest:
            largest = j
for i in matrix:
    for j in i:
        if j < smallest:
            smallest = j
prod = 1
for i in matrix:
    for j in i:
        prod*=j
print(row*col)
print(matrix)
print(largest)
print(smallest)
print(prod)