# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:59:11 2019

@author: saib

org=a.lower().split(",")
print(org)
b=a.lower().split(",")

print(b)

c=''
for s in b:
    c=c+s

print(c[::-1])

"""

a="A man, a plan, a canal; Panama"
b=list(a.lower())
alphas = list(filter(lambda x:x.isalpha(),b))
print(alphas)
print("True" if alphas==alphas[::-1] else "False")
