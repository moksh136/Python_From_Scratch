"""6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)"""
n = int(input("Enter number of products: "))

products = []

for i in range(n):
    product_id, product_name, price = input().split()

    product = (product_id, product_name, int(price))
    products.append(product)

print("\nAll Products:")
for product in products:
    print(product)

# Costliest Product
costliest = products[0]

for product in products:
    if product[2] > costliest[2]:
        costliest = product

print("\nCostliest Product:")
print(costliest)

# Cheapest Product
cheapest = products[0]

for product in products:
    if product[2] < cheapest[2]:
        cheapest = product

print("\nCheapest Product:")
print(cheapest)

# Average Price
total = 0

for product in products:
    total += product[2]

average = total / n

print("\nAverage Price:")
print(average)

# Products Above ₹50,000
print("\nProducts Above ₹50,000:")
for product in products:
    if product[2] > 50000:
        print(product)