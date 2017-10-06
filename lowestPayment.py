#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:34:36 2017

@author: iya
"""

balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
monthlyPayment = 10

testBalance = balance

while True:
    for month in range(1, 13):
        unpaidBalance = balance - monthlyPayment
        balance = round(unpaidBalance + monthlyInterestRate*unpaidBalance, 2)
    if (balance <= 0):
        break
    #print(str(monthlyPayment) + ": " + str(balance))
    monthlyPayment += 10
    balance = testBalance

print("Lowest payment: " + str(monthlyPayment))