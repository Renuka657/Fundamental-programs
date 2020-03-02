# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:09:29 2020

@author: lenovo
"""

#Program to enter P, T, R and calculate simple interest

P = float(input("Enter the principle amount:"))
T = float(input("Enter the time in years:"))
R = float(input("Enter the rate of interest:"))
SI = P * T * R / 100
print("simple interest:", SI)
