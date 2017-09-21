# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Assume s is a string of lower case characters.

# The program that prints the longest substring of s in which the letters occur in alphabetical order.

#s = 'azcbobobegghakl'
#s = 'abcbcd'
s = 'abcdefghijklmnopqrstuvwxyz'

maxabc = s[0]
if len(s) == 1:
    print('Longest substring in alphabetical order is: ' + str(maxabc))
else:
    index = 0
    
    for letter in s:
        index += 1
        if index > len(s):
            break
        left = letter
        curr_max = left
        print('Letter=' + left)
        print('Index=' + str(index))
        
        counter = index
        length = len(s)
        for right in s[index:]:
            counter += 1
            print('right='+right)
            print('index=' + str(index))
            if left <= right:
                curr_max += right
                print('curr_max=' + curr_max)
                left = right
                if counter == length and len(curr_max) > len(maxabc):
                    maxabc = curr_max
                    index = counter
                    break
            else:
                print('new max=' + curr_max)
                if len(curr_max) > len(maxabc):
                    maxabc = curr_max
                    index = counter
                break
    print('Longest substring in alphabetical order is: ' + str(maxabc))