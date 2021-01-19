# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:31:01 2020

@author: uha18
"""
'''
Implement a function gcd(x, y) that computes the greatest common divisor 
of x and y. (1 Point)

>>> gcd(8, 12)
4

'''
def euclgcd(m,n):
    if m<n:
        return euclgcd(n,m) #just to avoid exceptions if the first number is greater than the second one
    else:
        while n != 0:
            (m,n) = (n, m%n)
        return (m)
m = int(input("First number:"))
n = int(input('Second number:'))
print ('The greatest common devisor is: {0}'.format(euclgcd(m, n)))



# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test gcd ***')
    print('Test1', euclgcd(8, 12) == 4)
    print('Test2', euclgcd(42, 56) == 14)
    print('Test3', euclgcd(1071, 1029) == 21)
