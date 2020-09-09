# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:22:43 2020

@author: lenovo
"""

def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

b = fibon(10)
print(b)