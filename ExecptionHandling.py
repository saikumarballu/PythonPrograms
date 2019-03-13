# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:52:35 2019

@author: saib


while True:
    try:
        print(int(input("Please enter a number")))
        break
    except ValueError:
        print("It is not valid number")




##User Defined Exceptions

try:
    raise Exception('span','eggs')
except Exception as inst:
    print(inst.args)
    
    
"""
import sys
try:
    f = open("myfile.txt")
    val = int(f.readline())
except FileNotFoundError:
    print("No Such File")
except ZeroDivisionError:
    print("Divison by Zero")
except ValueError:
    print("Not a Number")
except:
    print(sys.exc_info())
    raise
else:           #The block contains statements which will execute safely or we can't forsee the execution
    print(6/val)
    f.close()
finally:
    print("finally Block")