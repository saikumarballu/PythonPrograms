# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:41:06 2019

@author: saib

Description: Remove Duplicates from a list
"""

b=[1,2,3,4,5,6,6,3,4]
c=b*3

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


def remdup2(a):
    nodup=[]
    print("List with Duplicates",a)
    for var in a:
        if var in nodup:
            pass
        else:
            nodup.append(var)
    return nodup

print("List without Duplicates:",remdup2(c))
        
    
    