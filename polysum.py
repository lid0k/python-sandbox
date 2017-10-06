#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:34:36 2017

@author: iya
"""

from math import tan, pi

def polysum(n, s):
    '''
    This function should sum the area and square of the perimeter 
    of the regular polygon. The function returns the sum, 
    rounded to 4 decimal places.
    '''
    def perimeter(n, s):
        return n*s
    def area(n, s):
        return (0.25*n*s*s)/tan(pi/n)
    return round((perimeter(n, s)**2 + area(n, s)),4)

print(polysum(4,5))