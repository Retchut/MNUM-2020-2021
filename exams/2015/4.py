# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:33:25 2021

@author: Retch
"""

import math

def g(x): return 2*math.log(2*x)

def picard_peano(x0, n):
    print("initial guess:", x0)
    y0 = 0
    for i in range(n):
        y0 = g(x0)
        x0 = y0
        print("\niteration", i+1)
        print("x =", x0)
    
    return x0
    
x0 = 1.1
n = 1
x1 = picard_peano(x0, n)

res = x1 - x0
print(res)