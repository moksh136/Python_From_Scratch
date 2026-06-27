"""
2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum  
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.
   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.
   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14
6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.
7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"
---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------
Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit
Enter your choice: 1
Enter rows: 3
Enter columns: 3
Enter matrix elements:
2 4 5
6 7 8
11 28 13
Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2
---------------------------------------------------------
Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit
Enter your choice: 2
Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0
---------------------------------------------------------
Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit
Enter your choice: 3
Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52
---------------------------------------------------------
Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit
Enter your choice: 4
Output:
Thank You for Using Matrix Analysis System
========================================================="""
rows = int(input("enter rows:"))
col = int(input("enter columns:"))
mat = []
print("for mat 1")
for i in range (rows):
    row = []
    for j in range(col):
        row.append(int(input()))
    mat.append(row)
while True:
    print("""1. Count Prime Numbers Row-wise
    2. Count Perfect Numbers Column-wise
    3. Display Row-wise Sum
    4. Exit""")
    choice = int(input("enter your choice:"))
    match choice:
        case 1:
            k = 1
            for i in mat:
                count = 0
                for j in i:
                    prime = True
                    if j == 1:
                        prime = False
                    else:
                        for k in range(2,j):
                            if j%k == 0:
                                prime = False
                                break
                    if prime:
                        count+=1
                print("row" ,k ,"prime Number Count :", count)
                k+=1
        case 2:
            k = 1
            for i in range(col):
                count = 0
                for j in range(rows):
                    sum = 0
                    for k in range(1, mat[j][i]):
                        if mat[j][i]%k == 0:
                            sum+=k
                    if sum == mat[j][i]:
                        count+=1
                print("Column", k ,"Perfect Number Count:",count)
                k+=1
        case 3:
            k = 1
            for i in mat:
                sum = 0
                for j in i:
                    sum+=j
                print("sum of", k , sum)
                k+=1
        case 4:
            print("Thank You for Using Matrix Analysis System")
            break


  