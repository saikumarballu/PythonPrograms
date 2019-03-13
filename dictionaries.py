# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:08:42 2019

@author: saib

"""

a = [1,2,3,4,5,6,7,1,1]
b = [1,2,3,4,5,6,7,1,1]

#c={name=['sai','kumar','ballu','hello'],id=[1,2,3,4]}

d= {'name':'sai','idd':1234,'pass':'password','extn':3211}
d['name']='kumar'
d['cel']=87686876
print(d)

del d['name']

#print(d.fromkeys.__doc__)

d.pop('idd')
print(d)