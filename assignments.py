# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:41:06 2019

@author: saib

Description: Remove Duplicates from a list
"""

b=[1,2,3,4,5,6,6,3,4]

def remdup(a):
    nodup=[]
    print("List with Duplicates",a)
    myset = set(a)
    print("set",myset)
    for var in a:
        if var in myset:
            nodup.append(var)
            myset.remove(var)
        if not myset:
            break
    return nodup
print(remdup(b))
        
    
    