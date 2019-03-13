# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:37:35 2019

@author: saib


def products(x,y):
    return x + y
a,b = 5,10

print("result=", products(a,b))

res=lambda x,y : x * y
print(res(a,b))



abc= lambda x,y : (2*x + 3*y) + (2*y + 3*x)
print(abc(a,b))

def welcome(name):
    print("Hello", name)

def welcome(a=2,name='sai'):
    print("Welcome", name)
welcome('kumar') # this will override the existing default arg
welcome() # this will use default argument
    
def myfunction(a=1,b=20,c='HI'):
    print(a+b)
    return c
print(myfunction(a=10,b=30,c='Hello')) 

print(myfunction(10,b=30,c='Hello'))  # Allowed
#print(myfunction(a=10,30,c='Hello'))  # Not Allowed

print(myfunction(b=10))  # Not Allowed




def varargs(*arg):
    print(arg )
varargs(12,23,34)
    
a=[1,2,3,4,5]
print(len(a))



def varkargs(*args, **kargs): # pass any number of non keywords & Keyword values
    print("non Keywords are ", args)
    print("Keywords are ", kargs)
print("With only non Keywords")
varkargs('a',4,5.6)

print("With  Keywords")
varkargs(a=10,b=20)

print("With only non Keywords")
varkargs('a',4,5.6,cd=12,ad='hello')



#Calling functional within a function
def square(x):
    return x**3
def applier(q,x):
    print(q,x)
    return q(x)

print(applier(square,9))

def doubleof(x):
    return x+x
print(applier(doubleof,9))




def applier(q,x,y):
    return q(x,y)

print(applier(lambda x, y: x + y,5,6))


def myfunc(n):
  return lambda a : n + a

mydoubler = myfunc(2) # This will return the lambda function here
# mydoubler = lambda a: a * 2

print(mydoubler(11))

ch = myfunc('https://')
ie = myfunc('http://')
print(ch('www.google.com'))
print(ie('www.google.com'))
"""

