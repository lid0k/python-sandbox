#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:34:36 2017

@author: iya
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1 and char == aStr:
        return True
    if char == aStr[len(aStr)//2]:
        return True
    else:
        middle = len(aStr)//2
        if char < aStr[middle]:
            return isIn(char, aStr[0:middle])
        else:
            return isIn(char, aStr[middle+1:])
   
print(isIn('x', 'xyz'))
print(isIn('a', 'abc'))
print(isIn('l', 'mooz'))
print(isIn('k', 'chkmy'))
        