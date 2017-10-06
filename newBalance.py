#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:34:36 2017

@author: iya
"""


def monthlyPayment(balance, monthlyPaymentRate):
    return round(monthlyPaymentRate*balance, 2)

def getNewBalance(balance, monthlyPaymentRate, annualInterestRate):
    unpaidBalance = balance - monthlyPayment(balance, monthlyPaymentRate)
    return round(unpaidBalance + annualInterestRate/12*unpaidBalance, 2)

def calculateMonthly(balance, monthlyPaymentRate, annualInterestRate):
    for month in range(1, 13):
        balance = getNewBalance(balance, monthlyPaymentRate, annualInterestRate)
        #print(str(month) + " : " + str(balance))
    print("Remaining balance: " + str(balance))
        
# TESTS

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

calculateMonthly(balance, monthlyPaymentRate, annualInterestRate)

