# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:32:50 2020

@author: uha18
"""

'''
Implement a function that recognizes palindromes (2 Points).

>>> is_palindrome("level")
True
>>> is_palindrome("levels")
False

Hints:

string[i] gives you the ith character from left (starting from 0)

string[-i] gives you ith character from right (starting from 1)

>>> s = "abcd"
>>> s[0]
a
>>> s[-1]
d

Integer division:

>>> 5 // 2
2

'''


def is_palindrome(word:str):
    fw = slice(word[0:len(word):1])
    bw = slice(word[-1:(-len(word)-1):-1])
    if fw == bw:
        return(True)
    else:
        return(False)
#print(is_palindrome(input()))


# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test is_palindrome ***')
    print('Test1', is_palindrome("level") == True)
    print('Test2', is_palindrome("levels") == False)
    print('Test3', is_palindrome("abba") == True)
    print('Test4', is_palindrome("aba") == True)
    print('Test5', is_palindrome("abab") == False)
    print('Test6', is_palindrome("") == True)
    print('Test7', is_palindrome("abxcba") == False) 