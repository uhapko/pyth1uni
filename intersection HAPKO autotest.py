# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:28:21 2020

@author: uha18
"""

'''

Implement a function that computes the intersection of two lists, i.e. a
function that returns a list of elements that are members of both input-lists.
(2 Points)

>>> intersection([1, 2, 3, 4], [2, 4, 6])
[2, 4]

Hints and comments:

x = [] creates an empty list

x.append(y) adds y to list x

>>> x = []
>>> x.append(1)
>>> x
[1]
>>> x.append(2)
>>> x
[1, 2]
'''


# ... your code ...
    
def is_member(a, t): #this is my function I wrote to complete a previous assignement
        for b in t:
            if a == b:
                return True
        return False
def intersection(x, y):
        intlist = []
        for m in x:
            if is_member(m, y) == True:
                intlist.append(m)
            if is_member(m, y) == False:
                continue
        return(intlist)
                
            

    


# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test intersection ***')
    print('Test1', sorted(intersection([1, 2, 3], [3, 2, 1])) == [1,2,3])
    print('Test2', sorted(intersection([1, 2, 3], [2, 3])) == [2,3])
    print('Test3', sorted(intersection([1, 2, 3], [4])) == [])
    print('Test4', sorted(intersection([], [4])) == [])


