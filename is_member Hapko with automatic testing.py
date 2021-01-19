# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:38:25 2020

@author: uha18
"""

def is_member(a, t):
    for b in t:
        if a == b:
            return True
            #break
    else:
        return False

# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test is_member ***')
    print('Test1', is_member(2, [1, 2, 3]) == True)
    print('Test2', is_member(4, [1, 2, 3]) == False)
    print('Test1', is_member(2, []) == False)