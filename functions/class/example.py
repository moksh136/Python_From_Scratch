"""def hello():
    print("this is first function")
hello()
"""
"""hello()
def hello(): # it gives an error bcoz funcn is not defined
    print("this is first function")
"""
"""
def sum():
    a = 10
    b = 20
    c = a+b
    print("sum is:", c)
sum()
"""
"""def sum(x, y): 
    c = x+y
    print("sum is:", c)
a = int(input("a"))
b = int(input("b"))
sum(a, b)"""
"""
def welcome():
    print("welcome")
def hello():
    print("hello guys")
    welcome()
def sum(x, y): 
    hello()
    c = x+y
    print("sum is:", c)
a = int(input("a"))
b = int(input("b"))
sum(a, b)
"""
"""def welcome(name):
    print("welcome", name)
def hello(name):
    print("hello", name)
    welcome(name)
    print("good bye")
hello("deepika")
"""
                # positional arg:
"""this arg are assigned based on their position"""

"""def hello(name, age):
    print("name is", name , "age is ", age)
hello(24, "moksh") #name is 24 age is  moksh
hello("sikha", 13) #name is sikha age is  13"""
"""
def mul(a, b):
    c = a*b
    return c
def sum(a, b):
    c = a+b
    return c 
def mainlogic():
    x = sum(10, 20) 
    y = mul(3,4)
    print("sum is", x)
    print("mul is", y)
mainlogic()
"""

"""def sum (a,b):
    c = a+b
    return c
def main():
    x = sum (10, 20)
    c = sum(11, 22)
    print(sum(66, 77))
    print(c)
    print(x)
main()"""

"""def hello():
    print("hello")
    return
    print("bye") # this line will not called by the function

def main():
    print("welcome")
    hello()
    print("done")"""

#returning multiple value
"""def calculate(a, b):
    return a+b, a-b
def main():
    print("welcome")
    res = calculate(10, 5)
    print(res)
    print("sum is", res[0])
    print("diff is", res[1])
    # by unpacking
    sum,diff = calculate(10, 5)
    print("sum is", sum)
    print("diff is", diff)
main()"""

# even value
"""def evenlist(n):
    even = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even.append(i)
    return even
def main():
    print(evenlist(10))
    x = evenlist(10)
    print(x)
main()


def evenlist(n):
    return n
def main():
    x = evenlist([10 , 20, 30 , 30])
    print(x)
main()"""

#keyword argumenyt
"""def hello(name, age):
    print("name is ", name)
    print("age is:", age)
hello(name="ram", age = 50)
#hello(name1 = "ram", age = 50) # hello() got an unexpected keyword argument 'name1'. Did you mean 'name'?
#hello(age = 50, "ram") #we can mix positional arg and keyword arg
hello("ram", age = 50, )"""

"""#default parameter
def hello(name , age , add= "indore" , sal= 40000):
    print("name is ",name)
    print("age is ", age)
    print("add is", add)
    print("sal ", sal)
hello("ram", 30)
hello("ram", 30, add = "chhennai", sal = 50000)

def hello(name = "sam", age , add= "indore" , sal= 40000): #error! parameter without a default follows parameter with a default
    print("name is ",name)
    print("age is ", age)
    print("add is", add)
    print("sal ", sal)
hello("ram", 30)
hello("ram", 30, add = "chhennai", sal = 50000) """


#variable lenght arg:
"""def display(*args):
    print(args)
display(1,2,3,4,5)
display("a", 2, 2.0, "ram")"""

"""def sum (*a):
    total = 0
    for n in a :
        total+=n
    print(total)
sum(1,2,3,4,56,7)"""
 
#write a menu driven program read 2 no and choise from user/choice 1 addition using diff fun/c2 sub 
# /c3 mul 
"""
def sum(a, b):
    c = a+b
    return c
def sub(a, b):
    c = a-b
    return c
def mul(a, b):
    c = a*b
    return c
def main(a,b):
    choice = int(input())
    a = int(input())
    b = int(input())
    if choice==1:
        sum(a,b)
    elif choice==2:
        sub(a,b)
    elif choice==3:
        mul(a,b)
main(a,b)"""

"""def hello(name, *marks):
    print(name)
    print(marks)
    print(*marks)
hello("ram", 10, 20, 40 )"""

"""def avg(*n):
    return sum(n)/len(n)
print(avg(10, 20, 30))"""

#passing list into *args
"""l = [1, 2, 3, 4]
def add(a,b,c,d):
    return a+b+c+d
print(add(*l))"""

"""def add(*l):
    s=0
    for i in l:
        s+=i
    return s
print(add(1,2,3,4,5,6))"""

"""l = [1, 2, 3, 4]
def add(*l1):
    return sum(l1)
print(add(*l))"""

#keyword variable length argument(**kwargs)
"""def display(**kwargs):
    print(kwargs)
display(name = "deepi", age = 60, add= "illahabad")
"""

"""def display(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
display(name = "deepi", age = 60, add= "illahabad")"""

"""def display(name,**kwargs):
    print(name, kwargs)
display(name = "deepi", age = 60, add= "illahabad")"""

"""def profile(**info):
    if "name" in info:
        print("welcome", info["name"])
    if "email" in info:
        print("email", info["email"])
profile(name= "deepo", email = "jee@email.com", add = "chennai")"""

#positional only para
"""def display (name, age,/):
    print(name, age)
display("deepi", 47)
display(name= "deepi", age= 47)""" #display() got some positional-only arguments passed as keyword arguments: 'name, age'

#keyword only para
"""def display (name,*, age, add):
    print(name, age, add)

display("deepi", age= 47, add = "chennai")"""

#combo of both
"""def show(id , name, /, salary, *, age ,add):
    print(id)
    print(name)
    print(salary)
    print(age)
    print(add)
show(101, "deepu", 3000, age = 30, add = "chennai")"""


def sum(a, b):
    c = a+b
    return c 
def xyz():
    print(sum(1,2))
    x = sum(1,2)
    print(x)

xyz()