# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:17:39 2020

@author: lenovo
"""

#Program to enter two angles of a triangle and find third angle

a = int(input("Enter the first angle:"))
b = int(input("Enter the second angle:"))
c = 180 - (a+b)
print("third angle:", c)