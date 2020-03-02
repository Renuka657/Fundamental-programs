# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:43:09 2020

@author: lenovo
"""

#Program to enter P, T, R and calculate compound interest

P = float(input("Enter the priciple amount:"))
T = float(input("Enter the time in years:"))
R = float(input("Enter the rate of interest:"))
CI = P * (pow((1 + R / 100) , T))
print("Compound interest:", CI)