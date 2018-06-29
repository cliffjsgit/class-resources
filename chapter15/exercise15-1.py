#!/usr/bin/env python3

__author__ = "Your Name"

import math
import copy

###############################################################################
#
# Exercise 15.1
#
#
# 1. Write a definition for a class named Circle with attributes center and 
# radius, where center is a Point object and radius is a number.
class Circle:
    '''junk'''
    
class Point:
    '''junk'''

class Rectangle:
    '''more junk'''

# 2. Instantiate a Circle object that represents a circle with its center at 
# (150, 100) and radius 75.

cir = Circle()
cir.center = Point()
cir.center.x = 150
cir.center.y = 100
cir.radius = 75


# 3. Write a function named point_in_circle that takes a Circle and a Point and 
# returns True if the Point lies in or on the boundary of the circle.

def point_in_circle(circle,point):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist <= circle.radius

p1 = Point()
p1.x = 160
p1.y = 110
p2 = Point()
p2.x = 5000
p2.y = 3300


# 4. Write a function named rect_in_circle that takes a Circle and a Rectangle 
# and returns True if the Rectangle lies entirely in or on the boundary of the 
# circle.

def rect_in_circle(circle,rectangle):
    p = copy.copy(rectangle.corner)
    if not point_in_circle(circle,p):
        return False
    p.x += rectangle.width
    if not point_in_circle(circle,p):
        return False
    p.y += rectangle.height
    if not point_in_circle(circle,p):
        return False
    p.x -= rectangle.width
    if not point_in_circle(circle,p):
        return False
    return True


rect = Rectangle()
rect.corner = Point()
rect.corner.x = 150
rect.corner.y = 100
rect.width = 50
rect.height = 50

print(rect_in_circle(cir, rect))

# 5. Write a function named rect_circle_overlap that takes a Circle and a 
# Rectangle and returns True if any of the corners of the Rectangle fall inside 
# the circle. Or as a more challenging version, return True if any part of the 
# Rectangle falls inside the circle.

def rect_circle_overlap(cir, rect):
    p = copy.copy(rect.corner)
    if point_in_circle(cir,p):
        return True
    p.x += rect.width
    if point_in_circle(cir,p):
        return True
    p.y += rect.height
    if point_in_circle(cir,p):
        return True
    p.x -= rect.width
    if point_in_circle(cir,p):
        return True
    return False
    
def rect_circle_corner_intrude(cir, rect):
    p = copy.copy(rect.corner)
    if not point_in_circle(cir,p):
        p.x += rect.width
        if not point_in_circle(cir,p):
            p.y += rect.height
            if not point_in_circle(cir,p):
                p.x -= rect.width
                if not point_in_circle(cir,p):
                    return False
    return True