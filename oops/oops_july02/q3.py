"""Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0"""

class Product:
    def __init__(self, product_id, product_name, quantity, price_per_item):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_item = price_per_item
    def calculate(self):
        self.total_amount = self.price_per_item * self.quantity
        if self.total_amount> 5000:
            self.discount = self.total_amount * 0.1
        else:
            self.discount = self.total_amount* 0.05
        self.final_amount = self.total_amount - self.discount
    def display(self):
        print("------ shopping Bill ------")
        print("product name :", self.product_name)
        print("product id :", self.product_id)
        print("quantity :", self.quantity)
        print("price per item:", self.price_per_item)
        print("total amount:", self.total_amount)
        print("Discount :", self.discount)
        print("final amount:", self.final_amount)
id = input("enter id:")
name = input("enter name:")
quantity = int(input("emter quantity:"))
price = int(input("enter price:"))
s1 = Product(id, name, quantity, price)
s1.calculate()
s1.display()