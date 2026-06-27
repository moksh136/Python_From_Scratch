"""1.
=========================================
ONLINE SHOPPING CART
=========================================
A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased
Write a program to:
* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.
Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}
Sample Output:
Total Quantity = 6
---"""
d = {}
n = int(input("enter no of student:"))
i = 1
while i<=n:
    product = input("enter name:")
    quantity = int(input("enter % of studet:"))
    d[product]= quantity
    i+=1
sum = 0
for key, values in d.items():
    sum+=values

print(sum)
