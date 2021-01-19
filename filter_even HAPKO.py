# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:51:23 2020

@author: uha18
"""

'''
2 Points

Implement a function that, when applied to a list of numbers, returns
a list of all even numbers in the original list, preserving their
order:

>>> filter_even([1,2,3,4,5,6,7,8])
[2,4,6,8]

'''

def filter_even(l):
    even = []
    for m in l:
        if int(m) % 2 == 0:
            even.append (m)
    return (even)


if __name__ == '__main__':
        print(filter_even([1,2,3,4,5,6,7,8]) == [2,4,6,8])
        print(filter_even([8,7,6,5,4,3,2,1]) == [8,6,4,2])
        print(filter_even([1,3,5,7]) == [])
