import time
import datetime

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def typing_speed_test(sentence):
    print(f"Type this sentence:\n{sentence}")
    start = time.time()
    input()
    end = time.time()
    time_taken = end - start
    words = len(sentence.split())
    wpm = round((words / time_taken) * 60, 2)
    return wpm