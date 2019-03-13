# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:35:50 2019

@author: saib

Description: Tuples, Lists and Strings
"""

list1 = [12,'hi',23.98,-12, ('hello',12),8]

tuple1 = (12,'dfs',5.3, [4,5,'sd'],-4,6)

greetings = "Good Morning"

# Counting starts with 0 and reverse counting will be from -1

print(list1[1:5]) # prints list1[0 to 5-1]

print(list1[:4])

print(tuple1[3:])

print(list1[-1:])

list2=list1
list3=list1[:]

print("list1 is",id(list1))
print("list2 is",id(list2))
print("list3 is",id(list3))

alphabets = 'abcdefghijklmnopqrstuvwxyz'

print(alphabets[0:26:3]) # it will skip every 4-1 elements output: aeimquy

print(alphabets[::-1]) # prints the reverse of the list

print(alphabets[:20:-1])


#list1 = [12,'hi',23.98,-12, ('hello',12),8]

#print hello from above list

print(list1[4][0])










