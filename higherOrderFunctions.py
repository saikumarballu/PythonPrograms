# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:00:15 2019

@author: saib

"""
def square(x):
    return x*x

def even(x):
    return 0 == x % 2

print(list(map(square,range(10,20)))) # map(function_name, arguments to pass to the function)

print(list(filter(even,range(10,20)))) # filter(returns number if the condition is True)

print(list(map(square,filter(even,range(10,20)))))



print(list(map(lambda x: x*x, range(10,20))))

print(list(filter(lambda x: x % 2 == 0, range(10,20))))