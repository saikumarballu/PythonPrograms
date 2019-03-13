# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:33:52 2019

@author: saib
"""

class Student:
    total = 1
    def __init__(self, n, a):
        self.__full_name=n
        self.age=a
        self.rollno = self.__class__.total
        self.__class__.total += 1
        
    def inc_age(self, c):
        self.age+=c
    def __repr__(self):
        return "Student"
    def __gt__(self, other):
        return self.age > other.age
    def get_name(self):
        return self.__full_name

class child_class(Student):
    def __init__ (self, n,a,s):
        Student.__init__(self,n,a)
        self.section = s
