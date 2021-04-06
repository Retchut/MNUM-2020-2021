# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:15:38 2021

@author: Retch
"""

import math

#bissection method

#the function
def f(x):
    return math.sin(x) + x**5 - 0.2 * x + 1

def bissection(a0, b0, func, max_it):
    
    sol = 0
    a = a0
    b = b0
    
    for n in range(0, max_it, 1):
        
        m = (a+b)/2
        sol = func(m)
        
        if sol*func(a0)<0:
            b = m
        elif sol*func(b0) < 0:
            a = m
            
    return m

def abs_err(xe, xap):
    return abs(xe-xap)

def rel_err(xe,xap):
    return abs(abs_err(xe,xap)/xe)
    
it = 6  #number of iterations
a = -1
b = 0

root = bissection(a, b, f, it)
exact = bissection(a,b, f, 100)
err1 = abs_err(exact, root)
err2 = rel_err(exact, root)

print("aproximated root is: " + str(root))
print("absolute error is: " + str(err1))
print("relative error is: " + str(err2))