# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:39:06 2019

@author: saib
"""

from classes import Student,child_class
stu1 = Student("sai",25)
stu2 = child_class("saikumar",34,"A")
print("Name Is",stu1.get_name(),"Age is",stu1.age, stu1.rollno)
stu1.inc_age(3)
print("Name Is",stu1.get_name(),"Age is",stu1.age,stu1.rollno)

stu2.inc_age(10)
print("Name Is",stu2.get_name(),"Age is",stu2.age,"Section",stu2.section,stu2.rollno)
print(stu2)

print(stu1 > stu2) ## This works with __gt__
print(stu1 < stu2)

