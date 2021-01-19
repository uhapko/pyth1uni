# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:49:49 2020

@author: uha18
"""

def is_prime(x):
     if x == 1:         return (False)
     if x == 2:         return (True)
     for m in range(2, x-1):
            if x % m == 0:
                return (False)
                break
     else: return (True)
    
    # this is for automatic testing.

# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test is_prime ***')
    print('Test1', is_prime(1) == False)
    print('Test2', is_prime(2) == True)
    print('Test3', is_prime(3) == True)
    print('Test4', is_prime(4) == False)
    print('Test5', is_prime(5) == True)
    print('Test6', is_prime(11021) == False)