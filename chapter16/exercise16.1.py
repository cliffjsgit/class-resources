#!/usr/bin/env python3

__author__ = "Your Name"

from Time1 import *

###############################################################################
#
# Exercise 16.1
#
#
# 1. Write a function called mul_time that takes a Time object and a number and
# returns a new Time object that contains the product of the original Time and 
# the number.
# 
# Then use mul_time to write a function that takes a Time object that represents
# the finishing time in a race, and a number that represents the distance, and 
# returns a Time object that represents the average pace (time per mile).
#

def mul_time(t1,factor):
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)


time1 = Time()
time1.hour = 1
time1.minute = 5
time1.second = 10

newtime = mul_time(time1,3)
print(newtime.hour,newtime.minute,newtime.second)