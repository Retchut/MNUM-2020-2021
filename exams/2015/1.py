# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:44:19 2021

@author: Retch
"""

Ta = 37

def dT(t, T): return -0.25*(T-Ta)

def euler(x0, y0, dx, dyx, n):
    
    print("iteration x y")
    print(0, x0, y0)
    
    for i in range(n):
        
        dy = dx * dyx(x0, y0)
        print(dy)
        
        y0 += dy
        x0 += dx
        
        print(i+1, x0, y0)
    
    return [x0, y0]



T=3
t=5
step = 0.4
n = 2

print("last T:", euler(t, T, step, dT, n)[1])