"""Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0"""
class Guest:
    def __init__(self, guest_id, guest_name, number_of_day, room_charge_per_day):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.number_of_day = number_of_day
        self.room_charge_per_day = room_charge_per_day
    def calculate(self):
        self.room_bill = self.number_of_day * self.room_charge_per_day
        self.gst = self.room_bill * 0.12
        self.final_bill = self.room_bill + self.gst
    def display(self):
        print("------ Hotel Bill ------")
        print("guest id:", self.guest_id)
        print("guest name:", self.guest_name)
        print("number of day:", self.number_of_day)
        print("room charge per day:", self.room_charge_per_day)
        print("room bill:", self.room_bill)
        print("gst :", self.gst)
        print("final bill:", self.final_bill)

id = input("enter id:")
name = input("enter name:")
days = int(input("emter no of days:"))
charge = int(input("enter room charge:"))
a = Guest(id, name, days, charge)
a.calculate()
a.display()