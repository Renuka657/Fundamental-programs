# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:49:14 2020

@author: lenovo
"""

#Program to enter marks of five subjects and calculate total, average and percentage

english = float(input("Enter the english marks:"))
maths = float(input("Enter the maths marks:"))
science = float(input("Enter the science marks:"))
social = float(input("Enter the social marks:"))
history = float(input("Enter the history marks:"))
total = english + maths + science + social + history
average = total / 5
percentage = (total * 500) / 100
print("total marks:", total)
print("average:", average)
print("percentage:", percentage)

