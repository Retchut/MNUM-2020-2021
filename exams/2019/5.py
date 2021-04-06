# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:26:05 2021

@author: Retch
"""

import math as m

def f(x):
    return -5*m.cos(x)+m.sin(x)+10

def aurea(x1, x2, x3, x4, n):
    B = (m.sqrt(5) - 1) / 2
    A = B**2
    
    for i in range(0, n+1):
        
        x3 = x1 + A*(x2-x1)
        x4 = x1 + B*(x2-x1)
        
        print(x1,x2,x3,x4,f(x1),f(x2),f(x3),f(x4))
        
        
        if ( f(x3) > f(x4) ):
            x2 = x4
        else:
            x1 = x3
        
        
         

x1 = 2
x2 = 4
x3 = 2.76393
x4 = 3.23606



aurea(x1,x2,x3,x4, 2)