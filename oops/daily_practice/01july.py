"""class Student:
    def set(self, id, name, address):
        print("set is calle")
        self.id= id
        self.name = name
        self.address = address
    def display(self):
        print("display is called")
        print("id is ", self.id)
        print("name is ", self.name)
        print("add is ", self.address)

s1 = Student()
s1.set(101, "ram", "chennai")
s1.display()

s2 = Student()
s2.set(102, "sam", "hyedrabad")
s2.display()
######################################################
print("WAP to add two numbers using class and object")
class Addition:
    def set(self, a, b):
        self.a = a
        self.b = b
    def cal(self):
        self.c = self.a+ self.b
    def display(self):
        return self.c
s = Addition()
s.set(10, 20)
s.cal()
res = s.display()
print(res)
#########################################
print("constructor")
class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def display(self):
        print("name", self.name, "and age is ", self.age)
s1 = Student("deepika", 30 )
s1.display()
###########################################################
class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def display(self):
        print(self.a + self.b)
s = Addition(10 , 20)

s.display()
"""
"""import speechrecognition as sr
import pyttsx3
r=sr.Recognizer()                       

with sr.Microphone() as source:
    print("Speak Anything :")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("You said : {}".format(text))
        audio =pyttsx3.init()
        audio.say("{}".format(text))
        audio.runAndWait()
    except:
        print("Sorry could not recognize your voice")"""


"""class counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count = self.count+1
    def decrement(self):
        self.count = self.count-1
    def getcount(self):
        return self.count
    
c = counter()
c.increment()
c.increment()
print(c.getcount())
c.decrement()
c.increment()
c.increment()
print(c.getcount())"""

#example of instance variable
"""class Student:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
s1 = Student("deepika", 30)
s2 = Student("rashmika", 43)
print(s1.name)
print(s2.name)
s1.name = "padkone"
print(s1.name)
print(s2.name)"""

#example of class variable
"""class Student:
    clg = "IIT Delhi"
    def __init__(self, name):
        self.name = name
s1 = Student("deepika")
s2 = Student("virat")
print(s1.name)
print(s2.name)
print(s1.clg)
print(s2.clg)
Student.clg = "IIT Dholakpur"
print(s1.clg)
print(s2.clg)"""

"""class Student:
    clg = "IIT Delhi"
    def __init__(self, name, city):
        self.name = name
        self.city = city
s1 = Student("deepika", "chennai")
s2 = Student("virat", "guna")
print(s1.__dict__)
print(s2.__dict__)
s1.clg = "sait" # it will create a new instance in s1 obj
print(s1.__dict__)
print(s2.__dict__)"""

"""class Test :
    x = 10
t1 = Test()
t2 = Test()
t1.x = 90
print(t1.x)
print(t2.x)
Test.x = 900
print(t1.x)
print(t2.x)"""

"""class Test :
    def __init__(self):
        self.a = 10
        self.b = 20
    def m1(self):
        self.c = 30
        self.d = 40
t1 = Test()
t1.m1()
t1.e = 900
print(t1.__dict__)"""

"""class Test:
    a = 10
    def __init__(self):
        self.b = 20
        Test.c = 60
    def m1  (self):
        Test.d = 50

t1 = Test()
t1.m1()
t2 = Test()
print(t1.__dict__)
print(t2.a)
print(t2.c)
print(Test.__dict__)"""

"""class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        c = self.a +self.b
        print(c)
t1 = Test(20, 30)"""
"""class Calculator:
    @staticmethod
    def add(a, b):
        return a+b
c1 = Calculator()
print(c1.add(10,20))
print(Calculator.add(10,20))
print(Calculator.__dict__)
print(c1.__dict__)
"""
"""
class Student :
    clg = "IIT"
    def set(self,name):
        self.name = name
    @staticmethod
    def display (x):
        print(Student.clg)
        #print(name)
        #print(self.name)
        print(x.name)
c1 = Student()
c1.set("deepak")
c1.display(c1)
"""
#statistic
#regular expression
import re
text = "python is easuy"
res = re.match(r"python", text)
print(res)