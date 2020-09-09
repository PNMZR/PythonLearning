# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:09:46 2020

@author: lenovo
"""

def generator_function():
    for i in range(3):
        yield i

# for item in generator_function():
#     print(item)
    
    
gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen))

my_string = "Yasoob"
my_iter = iter(my_string)
print(next(my_iter))