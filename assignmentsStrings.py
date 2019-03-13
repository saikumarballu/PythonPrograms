# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:49:57 2019

@author: saib
"""

urls = ['a.in','b.hk','c.in','h.in','k.uk','us.com']

print(list(filter(lambda x : x.endswith('in'),urls)))
