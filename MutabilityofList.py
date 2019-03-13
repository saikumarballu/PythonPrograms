# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:23:23 2019

@author: saib

Operations on a List

"""

a = [1,2,3,4,5,6,7,1,1]
b = [8,9,10]

print(a)

a[1] = 'hi'

a.append(4)
a.append(['is','a','rela'])

print(a)

print(dir(a))

print(a.count.__doc__)

print(a.count(1))

#dir() will give the full detialed methods or system defined

a.insert(2,34) # inserts 34 at 2+1th position (3rd position in this case)

print(a) # output: [1, 'hi', 34, 3, 4, 5, 6, 7, 1, 1, 4]

a.extend([78,89,90]) # appends multiple values at the same time
print(a)

a=a+['hi','jk']

print(a)

print(a.index('hi'))



























