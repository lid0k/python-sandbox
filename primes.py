#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:45:18 2017

@author: iya
"""

def genPrimes():
    num = 1
    while(True):
        num += 1
        max = num//2 + 1
        for d in range(2, max):
            if num % d == 0:
                max = d
                # breaks as the divider is found
        if max == num//2 + 1:
            yield num


primes = genPrimes()
for i in range(0, 20):
    print(primes.__next__())      