# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:01:52 2019

@author: saib
"""

class sample:
    x = 1458
    def increment(self):
        self.__class__.x += 1

a = sample()
a.increment()
print(a.__class__.x)
print(a.x)