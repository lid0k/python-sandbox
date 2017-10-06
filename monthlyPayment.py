#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:34:36 2017

@author: iya

Code for edx MITx+6.00.1x
Using Bisection Search to Make the Program Faster

Find the smallest monthly payment to the cent 
such that we can pay off the debt within a year
using bisection search.
"""

#Test data
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12

lower = balance/12
upper = (balance*(1 + monthlyInterestRate)**12)/12

monthlyPayment = (upper + lower)/2
testBalance = balance

# Pay to the cent
epsilon = 0.01

while abs(lower-upper) > epsilon:
    #print('lower: ' + str(lower))
    #print('upper: ' + str(upper))
    #print('monthly: ' + str(monthlyPayment))
    #print('balance: ' + str(balance))
    for month in range(1, 13):
        unpaidBalance = balance - monthlyPayment
        balance = unpaidBalance + monthlyInterestRate*unpaidBalance
    #print(str(monthlyPayment) + ": " + str(balance))
    if balance > 0:
        temp = monthlyPayment
        monthlyPayment = (upper + monthlyPayment)/2
        lower = temp
        balance = testBalance
    elif balance < 0:
        temp = monthlyPayment
        monthlyPayment = (lower + monthlyPayment)/2
        upper = temp
        balance = testBalance
    else:  # for the improbable case we get exactly 0 balance 
        break

print("Lowest payment: " + str(round(monthlyPayment, 2)))