# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:28:01 2020

@author: uha18
"""

print('Welcome to the prime numbers finding program!')
print('Type in the number:')
x = int(input())
for n in range(2,x+1):
    for m in range(2, n):
        if (n % m) == 0:
            break
    else:
        print (n)
    

        