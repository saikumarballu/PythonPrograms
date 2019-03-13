# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:08:42 2019

@author: saib

"""

a = [1,2,3,4,5,6,7,1,1]
b = [88,98,100,5]

#c={name=['sai','kumar','ballu','hello'],id=[1,2,3,4]}
s1=set(a)
s2=set(b)
print(s1.union(s2))

print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
