# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:53:52 2021

@author: Retch
"""

import math

a = 2 #miro
#a = 1 #meu

def f(x):
    return (x-a)**2 + x**4

def aurea(x1,x2):
    B = (math.sqrt(5)-1)/2
    A = B**2
    while(abs(x2-x1) > 0.000001):
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        
        if f(x3) < f(x4):
            x2 = x4
        else:
            x1 = x3
    
    print( (x1 + x2) /2)

x1 = 0.5
x2 = 1

aurea(x1, x2)
    