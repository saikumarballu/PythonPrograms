# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:58:24 2019

@author: saib

Description: Find the value of a key in dictionary
"""

a={'a':1, 'ab':2,'abc':3}
k='a'

if k in a.keys():
    print(k,a[k])
else:
    print(k,"Doesn't Exist")


# find all the keys in the dictionary by given a value

def mydictvalues(dict,val):
    flag =0
    for (a,b) in dict.items():
        if val == b:
            print(a)
            flag=1
    if flag == 0:
            print("No Keys Found")
        
mydictvalues(a,4)     


    