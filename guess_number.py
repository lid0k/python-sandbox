#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:23:22 2017

@author: iya
"""

# Guesses the number you thought of with bisection search

import math
#print("NEW GAME:")
print('Please think of a number between 0 and 100!')
low = 0
guess = 50
high = 100

guessed = False
while not guessed:
    print('Is your secret number '+ str(guess) + '?')
    result = input("Enter 'h' to indicate the guess is too high." + 
      " Enter 'l' to indicate the guess is too low." + 
      " Enter 'c' to indicate I guessed correctly.")
    if result == 'c':
        guessed = True
    elif result == 'l':
        low = guess
        guess = math.floor((high + low)/2)
    elif result == 'h':
        high = guess
        guess = math.floor((high + low)/2)
    else:
        print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str(guess))