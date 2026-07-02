"""Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0"""
class Customert:
    def __init__(self, customer_id, customer_name, unit_consumed):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.unit_consumed = unit_consumed
    def calculate(self):
        self.bill = (self.unit_consumed * 8 )+150
    def display(self):
        print("------ Electricity Bill ------")
        print("customer name :", self.customer_name)
        print("customer id :", self.customer_id)
        print("unit consumed", self.unit_consumed)
        print("bill:", self.bill)
id = input("enter id:")
name = input("enter name:")
unit = int(input("emter salary:"))
s1 = Customert(id, name, unit)
s1.calculate()
s1.display()