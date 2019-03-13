# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:40:10 2019

@author: saib
"""

a = [1,2,3,4,5,6,7,1,1]
b = [8,9,10]

print(a.index(1,-1))
print("a repeated for: ",a.count(1),"times")

a.remove(1) # will delete very first occurance of 1 in the list

print(a)

print(a[0:7:4])

a.pop()
print(a)

c=5.7,'ji',6,7,

print(c[:])

