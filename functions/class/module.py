#print(help("modules"))

"""import math
print(math.sqrt(46))
print(math.__doc__)
print(help(math))"""

"""import random
number = random.randint(1,10)
guess = int(input("enter n0:"))
if guess== number:
    print("vastunk huiyyaaan")
else:
    print("dubara try kr")"""

"""from datetime import date
today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)"""
"""from datetime import datetime
today = datetime.today()
f = today.strftime("%W")
print(f)
print(today)
print(today.year)
print(today.hour)
print(today.minute)"""

"""from datetime import datetime"""
"""str = input("enter date (dd-mm-yyy)")
dt = datetime.strptime(str, "%d-%m-%Y")
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)"""
"""
str = input("enter date (dd-mm-yyy)")
now = datetime.now()
dt = datetime.strptime(str, "%d-%m-%Y")
age = now.year - dt.year
print(age)"""

"""from datetime import datetime, timedelta
today = datetime.now()
print(today)
exp = today + timedelta(days = 7)
print(exp)

dob1 = datetime(2026, 2, 20)
dob2 = datetime(2024, 2, 20)
d = dob1 - dob2
print(d)
"""

"""import calendar
print(calendar.calendar(2026)) # it gives calender of respective year
print(calendar.month(2026,7))# it give respective month
print(calendar.weekday(2026, 7 , 18)) #it gives day
print(list(calendar.day_name))# it give list of day name
print(list(calendar.month_name))#it gives month name
print(calendar.isleap(2028))# it give year is leap or not"""


#import os
"""cwd = os.getcwd()
print(cwd)
os.mkdir("okayy")# cretes the folder
print("done")"""
"""print(os.listdir("."))#it give list of obj

os.rmdir("okayy") # it remove created folder or existing folder
"""
#print(os.getpid()) #it gives id of current processs
"""
import mymath as mm
print(mm.add(10, 20))"""

import mypackages
print("bhagooo")
mypackages.calculation()