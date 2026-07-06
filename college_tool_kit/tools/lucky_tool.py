import random
import calendar

def lucky_number():
    return random.randint(1, 100)

def birthday_weekday(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]