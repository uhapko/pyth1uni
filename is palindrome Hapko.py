# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:09:19 2020

@author: uha18
"""


def is_palindrome(word:str):
    fw = slice(word[0:len(word):1])
    bw = slice(word[-1:(-len(word)-1):-1])
    if fw == bw:
        return('palindrome')
    else:
        return('non-palindrome')
print(is_palindrome(input()))
   
    