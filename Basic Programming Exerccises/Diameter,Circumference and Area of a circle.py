# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:16:09 2020

@author: lenovo
"""

#Program to enter radius of a cirle and find it's diameter,circumference and area

radius = float(input("Enter radius of a circle:"))
PI = 3.14
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius
print("Diameter of a circle:", diameter)
print("Circumference of a circle:", circumference)
print("Area of a circle:", area)
