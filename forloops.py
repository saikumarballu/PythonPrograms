# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:03:31 2019

@author: saib
"""

dict1 = {'name':'Saikumar', 'id':1235, 'cell':92992992, 'extn':8768}

print(dict1.keys())
print(dict1.values())

# Traverse dictionary using the key values
for k in dict1.keys():
    print(k, "=>",dict1[k])
print(dict1.items())

# Traverse dictionary using the tuple
for (k,l) in dict1.items():
    print(k, "=>",l)


#
#for (k,l) in ([('name', 'Saikumar'), ('id', 1235), ('cell', 92992992), ('extn', 8768)]):
#    print(k, "=>",l)
#

