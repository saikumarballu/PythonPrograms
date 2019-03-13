# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:15:17 2019

@author: saib
"""

list1 = [1,2,3,34,5,6,90]
list2 = [8,7,6,5,4,3,78]

print(list(map(lambda x , y: x + y,list1, list2)))

print(list(zip(list1,list2)))
print(dict(zip(list1,list2)))

print(list(enumerate(list1,2)))

print([elem*2 for elem in list1])

list3= [('a',2), ('b',3),('c',4)]

print([n * 3 for (x,n) in list3])

def subtract(a,b):
    return a-b

numlist = [(1,2),(4,2),(8,4)]

print([subtract(x,y) for (x,y) in numlist])