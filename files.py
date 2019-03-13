# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 15:23:20 2019

@author: saib
"""

def file_wr(filename):
    f=open(filename,'w')
    f.write("Hi this is a file\n")
    f.write("How are you\n")
    f.write("How are you\n")    
    f.close()

#file_wr("C:\\Users\\saib\\Desktop\\SAI\\file.txt")
file_wr("file.txt")

def file_read(filename):
    f=open(filename)
    #print(f.readline())
    print(list(map(lambda x:x.strip(),f.readlines())))
    #print(f.read())
    f.close()

file_read("file.txt")