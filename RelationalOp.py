# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:35:54 2019

@author: saib
"""
def abcd():
    """
    abcd is a list comparison function
    """
    print(list1 is list2)
    print(list1 is list3)
    print(list1 == list3)
    print(list1 == list2)


list1= [1,2,3,4,5,6,7]
list2 = list1
list3 = list1[:]

abcd()

x,y,z = 5,10,15

# precedency: Not, and, or

print(x > 7 or y > 1 and z > 14)

name = input("Enter Your Name: ")

wage = int(input("Enter Your Wage: "))

print ("Hello ", name)
print ("Daily Wage is:", wage * 8)