"""=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3"""
n = int(input("Enter number of orders: "))

orders = []

for i in range(n):
    order_id, customer_name, product_name, amount = input().split()
    orders.append([order_id, customer_name, product_name, int(amount)])

# Display all orders
print("\nAll Order Details:")
for order in orders:
    print(order[0], order[1], order[2], order[3])

# Highest Value Order
highest = orders[0]

for order in orders:
    if order[3] > highest[3]:
        highest = order

print("\nHighest Value Order:")
print(highest[0], highest[1], highest[2], highest[3])

# Total Sales
total_sales = 0

for order in orders:
    total_sales += order[3]

print("\nTotal Sales:")
print(total_sales)

# Orders Above 10000
count = 0

for order in orders:
    if order[3] > 10000:
        count += 1

print("\nOrders Above ₹10,000:")
print(count)