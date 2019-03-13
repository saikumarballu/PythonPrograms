# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:14:04 2019

@author: saib

^ - Begining of String or expression
$ - Ending of String or an Expression
+ - One or more occurance of previous character
* - 



import re
pat1 = re.compile('^Hello')

mystr = "Hi Hello World"

if pat1.search(mystr):
    print("Matched")
else:
    print("Not Matched")

pat2 = re.compile('World$')    
if pat2.search(mystr):
    print("Matched")
else:
    print("Not Matched")
    


import re
#pat1 = re.compile('^\d{10}$') # Matching 10 digits
pat1 = re.compile('^(\+91)?\d{10}$') # '^(\+91) is optional and later it should have 10 digits
if pat1.search('+917894561230'): # '^\d+$' Matching any number of digits
    print("It is Number")
else:
    print("Not Just a Number")



import re
#pat1 = re.compile('^\d{10}$') # Matching 10 digits
pat1 = re.compile('^(\+91)?(\d{10})$') 
searchobj = pat1.search('+911234567890')
if searchobj:
    print(searchobj.group(0)) # Entire match
    print(searchobj.group(1)) # first Group
    print(searchobj.group(2)) # Second Group
    print("It is Number")
else:
    print("Not Just a Number")



p = re.compile('\d+')
print(p.findall('12 Number,11 pipes,10 Cars')) # returns only numbers in the string

email = re.copmile('(\w+)@(\w+\.com)')





import re
pat1=re.compile('^Hello',re.IGNORECASE) # ignore case while searching
email = re.copmile('(\w+)@(\w+\.com)')
mystr = "hello World"

if pat1.search(mystr):
    print("Matched")
else:
    print("Not Matched")

if pat1.search(mystr):
    print("Matched")
else:
    print("Not Matched")


import re
p= re.compile(r'\W+') # removes all non-words and returns only words
lists= p.split('This is a pattern split, simple and short, easier version of split().')


print(p.split('This is a pattern split, simple and short, easier version of split().',3))

"""
import re
p=re.compile('(blue|white|red)')

print(p.sub('color', 'blue socks and red shoes')) # Replace pattern with color
print(p.sub('color', 'blue socks and red shoes', count=1)) # Replace pattern with color


















