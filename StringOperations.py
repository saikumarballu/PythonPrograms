# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:03:10 2019

@author: saib


name="sai kumar"
print(name.title())
print(name.capitalize())
print(name.upper())

def yesno():
    ans = input("Enter yes or no: ").strip()
    if ans.upper() == "YES":
        print("You Typed Yes")
    elif ans.upper() == "NO":
        print("You Typed No")
    else:
        print("Please enter only Yes or No")
yesno()
    
"""
wage = input("Enter your wage")
print(type(wage))
print(wage.isdigit())
if wage.isdigit():
    wage=int(wage)
    print("Inside if")
print("Daily Wage is", wage*8)