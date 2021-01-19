# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:59:25 2020

@author: uha18
"""

from math import sqrt, pi 
def vol(r,h):
    return 1/3*pi*r**2*h

def sarea(r,h):
    return pi*r*sqrt(h**2+r**2) + pi*r**2
#here I didn't want to define the slant height as a separate function, that's why i just hardcoded it into two previous functions

print('I am a program capable of caclulating the volume and surface area of a cone using given geometrical parameters')
print('Now enter the radius of the cone:')
r = float(input())
if r<0:
    print ('Are you sure? The radius cannot be negative!')
else:
    print('Now enter the height of the cone:')
h = float(input())
if h<0:
        print ('Are you sure? The height cannot be negative!')
else:
    print('The surface are of the cone is {:.10f}, the volume being {:.10f}' .format(vol(r, h), sarea(r,h)))