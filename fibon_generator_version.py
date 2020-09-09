# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:19:59 2020

@author: lenovo
"""

# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        

for x in fibon(10):
    print(x)  


b = fibon(10)
print(b)      