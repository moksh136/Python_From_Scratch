#anonymous function/ lambda 
"""fun = lambda n:n*n
print(fun(5))"""

#write a lambda function to ad two function 
"""add = lambda a,b:a+b
print(add(10,39))

add = lambda a,b:print(a+b)
add(10,39)"""

"""max = lambda a,b:a if a>b else b
print(max(10, 30))"""


#MAP function :
"""def sq (x):
    return x*x 
l1 = [10, 20 , 30 ,40]
print(list(map(sq, l1)))"""

"""l = [1, 2, 3, 4]
r = map(lambda x:x*x, l)
print(list(r))"""

# by normal method
"""l = ["ram", "sam", "sid"]
def convert(s):
    return s.capitalize()
r = map(convert,l)
print(list(r))"""

#by lammbda function
"""l = ["ram", "sam", "sid"]
r = map(lambda a:a.capitalize(),l)
print(list(r))#['Ram', 'Sam', 'Sid']"""

"""l = ["ram", "sam", "sid"]
r = map(lambda a:a.upper(),l)
print(list(r))""" #['RAM', 'SAM', 'SID']

"""l = ["ram", "sam", "sid"]
r = map(lambda a:len(a),l)
print(list(r)) #[3, 3, 3]"""

#WAP a program to add two list
"""l1 = [1, 2, 3]
l2 = [4, 5, 6]
def add(a, b):
    return a+b
r = map(add,l1,l2)
print(list(r))"""

"""l1 = [1, 2, 3]
l2 = [4, 5, 6]
r = map(lambda a,b:a+b,l1,l2)
print(list(r))"""

"""l1 = [1, 2, 3]
r = map(lambda a: "even" if a%2==0 else "odd", l1)
print(list(r))"""

"""l1 = [57, 90, 75]
r = map(lambda a:"A" if a>= 90 else "B" if a>= 70 else "B" if a>= 50 else "D", l1)
print(list(r))"""

####filter function
#filter(function, iterable)

"""l = [96, 78, 45, 63]
def fun(x):
    return x%2 == 0
r = filter(fun, l)

r =filter(lambda x:x%2 ==0, l)
print(list(r))"""

"""l =["deep", "veeer", "moksh"]
r= filter(lambda a: a.startswith("m"), l)
print(list(r))"""

#WAP to filter only those name whose length is greater than 5
"""l = ["ram", "moksh", "sikhaa"]
r = filter(lambda a:len(a)>5, l)
print(list(r))"""

#wap to convert string num of list to integer
"""l = ["1", "2", "3"]
r = map(lambda a:(int(a)), l)
print(list(l))"""


#WAP to remove empty str from list
"""l = ["deep", "", "ram"]
r = filter(lambda a:len(a)!=0,l)
print(list(r))"""

"""l = [1, 2, 3, 4]
r = filter(lambda a:a%2==0,(map(lambda a:a*a, l)))
print(list(r))""" #[4, 16]

#WAP to rev each word of a list
"""l = ["ram", "sam", "moksh"]
r = map(lambda a:a[::-1], l)
print(list(r))"""

"""from functools import reduce
def add(a, b):
    return a+b
num = [1, 2, 3, 4, 5, 6]
res = reduce(add, num)
print(res)"""

"""from functools import reduce
num = [1, 2, 3, 4, 5, 6]
res = reduce(lambda x,y:x+y, num, 10)
print(res)"""
"""from functools import reduce
num = [1, 2, 3, 4, 5, 6]
res = reduce(lambda x,y:x if x>y else y, num)
print(res)"""


"""num = [7, 5, 9, 3, 5]
x = sorted (num , key = lambda x:x)
print(x)

name = ["ram", "moksh", "ab", "wxyz"]
x = sorted(name, key = lambda x:len(x))
print(x)"""

#RECURSIVE FUNCTION
"""def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)

def main():
    x = fact(5)
    print(x)
main()"""

#WAP to sum of n natural number using recursive function
"""def sum(n):
    if n == 0:
        return 0
    return n+sum(n-1)

def main():
    n = int(input("enter n:"))
    x = sum(n)
    print(x)
main()"""

#WAP for power using recursion 
"""def pow (b, p):
    if p == 0:
        return 1
    return b*pow(b, p-1)
def main ():
    x = pow (2, 5)
    print(x)
main()"""

#WAP to count digits in a number

"""def count(n):
    if n == 0:
        return 0
    return 1+count(n//10)

def main():
    x = count(12345)
    print(x)
main()"""

"""def hello(name):
    def message():
        return "hey ram"
    print ("hello", name)
    print(message())
hello("deepiaka")
"""
"""
def outer ():
    x = 10
    def inner():
        y = 20
        print("value of ", x)
    inner()
#   print(y) will gives error 
outer()"""

#nested functon
"""def total(price, taxrate):
    def calculatetax():
        return price*taxrate
    return price + calculatetax()
print(total(1000, 0.18))"""
"""
def bill(amount):
    def discount():
        if amount > 10000:
            return amount *0.10
        return 0
    d = discount()
    final = amount - d
    return final
print(bill(500000))"""

"""print("closure")

def counter():
    count = 0
    def increment ():
        nonlocal count
        count +=1
        return count
    return increment
c = counter()
print(c())
print(c())
print(c())

def card(greeting , name):
    def card():
        return f"{greeting},{name}"
    return card
first = card("hii", "deepika")
second = card("hii", "sikha")
print(first())
print(second())
print(first.__closure__)

#decorators
def mydesign(func):
    def wraper():
        print("before")
        func()
        print("after")
    return wraper
#first method
def hello():
    print("heyyyyyyyyyyyyyyyyy")

d = mydesign(hello)
d()

#second method
@mydesign
def hello():
    print("heyyyyyyyyyyyyyyyyyyyy")
hello()"""

loggedin = False/True
def loginreq(func):
    def wraper():
        if loggedin:
            func()
        else:
            print("login plz.......")
    return wraper

@loginreq
def profile():
    print("welcome to our page")
profile()

def mydecorator(func):
    def wrapper (*args, **kwargs):
        print("calculation")
        res = func(*args, **kwargs)
        print("done")
        return res
    return wrapper

@mydecorator
def add(a,b):
    print("sum is", a+b)
add(10, 20)

def add(a, b, c):
    print("sum is ", a+b+c)
add(10, 20, 30)

def add (a:int, b:int)-> int:
    return a+b

res = add(10.768553, 20)
print(res)