# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:09:57 2019

@author: saib
"""

class counter:
    overall_total = 0
    def __init__(self):
        self.mytotal = 0
    def increment(self):
        counter.overall_total += 1
        self.mytotal += 1
a = counter()
b = counter()
a.increment()
print(a.mytotal)
print(a.__class__.overall_total)
b.increment()
print(b.mytotal)
print(b.__class__.overall_total)
b.increment()
print(b.mytotal)
print(b.__class__.overall_total)
print(a.mytotal)
print(a.__class__.overall_total)
print(b.mytotal)
print(b.__class__.overall_total)