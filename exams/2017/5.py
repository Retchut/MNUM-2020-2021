# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:07:06 2021

@author: Retch
"""

def W(x,y): return -1.1*x*y + 12*y + 7*(x**2) - 8*x

def dWx(x,y): return -1.1*y + 14*x - 8
def dWy(x,y): return 12 - 1.1*x

def grad(x0, y0, l, n):
    print("iteration x y l")
    print(0, x0, y0, l)
    
    for i in range(n):
        dx = l * dWx(x0, y0)
        dy = l * dWy(x0, y0)
        
        x0 -= dx
        y0 -= dy
        
        print(i+1, x0, y0, l)
        
    return W(x0, y0)
        
x0 = 3
y0 = 1
l = 0.1
n = 1

print(grad(x0, y0, l, n))