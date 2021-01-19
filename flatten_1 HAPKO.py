# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:02:06 2020

@author: uha18
"""

'''
2 Points

Implement a function flatten1 that, when applied to a list of lists,
returns a list of all elements of the embedded lists, preserving their
order:

>>> flatten1([[1,2,3], [4,5,6], [7], [], [8, 9]]):
[1,2,3,4,5,6,7,8,9]

Note that flatten1 is not "recursive" i.e., when one of the embedded list
contains (one or more) other lists, these lists should not be "flattend":

>>> flatten1([[1,2,3], [[4,5,6], [7]], [], [8, 9]]):
[1,2,3,[4,5,6],[7],8,9]

'''
 
def flatten1(lol):
    fl = []
    for m in lol:
        if type(m) is list:
            for mm in m:
                fl.append(mm)
    return (fl)
            



if __name__ == '__main__':
    print(flatten1([[1,2,3], [4,5,6], [7], [], [8, 9]]) == [1,2,3,4,5,6,7,8,9])
    print(flatten1([[1,2,3], [[4,5,6], [7]], [], [8, 9]]) == [1,2,3,[4,5,6],[7],8,9])