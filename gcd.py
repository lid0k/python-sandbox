#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:34:36 2017

@author: iya
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b > a:
        t = b
        b = a
        a = t
        
    for t in range(b, -1, -1):
        if a % t == 0 and b % t == 0:
            return t
        t = t - 1
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        gcdRecur(b, a)
    if b == 0:
        return a
    return gcdRecur(b, a % b)

    
print(gcdIter(6,12))
print(gcdRecur(6,12))
        