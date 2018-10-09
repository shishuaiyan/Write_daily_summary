# -*- coding:utf-8 -*-
# __author__ = '32830'

a = '12:10:09'
b = '12:18:07'

def clock_subtraction(clock_minuend, clock_subtrahend):
    seconds = int(clock_minuend.split(':')[2]) - int(clock_subtrahend.split(':')[2])
    minutes = int(clock_minuend.split(':')[1]) - int(clock_subtrahend.split(':')[1])
    if seconds < 0:
        seconds += 60
        minutes -= 1
    print_str = str(minutes)+'分'+str(seconds)+'秒'
    print(print_str)


clock_subtraction(b, a)
