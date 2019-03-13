# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:20:24 2019

@author: saib
"""


class Student:
    def __init__(self, n, a):
        self.full_name=n
        self.age=a
    
    def inc_age(self, c):
        self.age+=c
        
        
class child_class(Student):
    def __init__ (self, n,a,s):
        Student.__init__(self,n,a)
        self.section = s
