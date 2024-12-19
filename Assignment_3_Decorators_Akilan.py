#Code author: Akilan
import logging
def my_decorator(func):
    def log(*args, **kwargs):
        """writes log message in console"""
        logging.info(*args, **kwargs)
        file=func(*args, **kwargs)
        print (file)
        return file
    return log

import time
def time_decorator(func):
    def time2(*args, **kwargs):
        """writes time taken to complete the function"""
        start_time=time.time()
        timetaken=func(*args, **kwargs)
        end_time=time.time()
        total=end_time-start_time
        print (f"{total}")
        return timetaken
    return time2

"""Using 2 decorator functions, which does write a log message first and then calculate the time taken to write the log message second"""
@time_decorator
@my_decorator
def message(input):
    return input

output=message("hi humans")