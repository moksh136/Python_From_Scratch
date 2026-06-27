"""6.
 Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number"""
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    else:
        return True
    
n = int(input("enter number:"))
def main():
    x = prime(n)
    if x :
        print("prime")
    else:
        print("nor")
main()