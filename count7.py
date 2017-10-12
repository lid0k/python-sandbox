#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:34:36 2017

@author: iya
"""


def count7(N):
    '''
    N: a non-negative integer
    '''
    #print("calling, N = " + str(N))
    if N < 1:
        return 0
    last = 0
    if N % 10 == 7:
        last = 1
    return count7(N // 10) + last
    
    
    
    
print(str(count7(717)))
print(str(count7(1237123)))
print(str(count7(8989)))