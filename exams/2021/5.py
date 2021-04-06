# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:49:00 2021

@author: Retch
"""

def f(x): return x**3 + 2*(x**2) + 10*x - 26
def df(x): return 3*(x**2)+4*x+10

def newton(x0,n):
    x = x0
    print("iteration 0: ", x)
    for i in range(n):
        x = x - f(x)/df(x)
        print("iteration " + str(i+1) +":", x)
        
guess = 0
it = 2

newton(guess, it)