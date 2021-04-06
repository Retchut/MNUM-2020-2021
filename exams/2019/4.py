# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:44:53 2021

@author: Retch
"""

def f(y, tempA):
    return -0.25*(y-tempA)

def euler(x0, y0, tempA, dx, steps):
    x = x0
    y = y0
    print("step: 0\t t = " + str(x) + "\t temp = " + str(y))
    
    for n in range(0, steps):
        x += dx
        
        dy = f(y, tempA) * dx
        y += dy
        
        print("step: " + str(n + 1) + "\t t = " + str(x) + "\t temp = " + str(y))
    return


temp = 2
tempA = 59
t = 2
h = 0.5
n = 2

final_temp = euler(t, temp, tempA, h, n)
