# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:40:42 2021

@author: Retch
"""

def f(x,y):
    
    if x==0:
        if y == 0: return 1.1
        elif y == 1: return 2.1
        elif y == 2: return 7.8
        
    elif x == 1:
        if y == 0: return 1.4
        elif y == 1: return 4
        elif y == 2: return 1.5
        
    elif x == 2:
        if y == 0: return 9.8
        elif y == 1: return 2.2
        elif y == 2: return 1.2
            
def simp_sys(x0, y0, xf, yf):
    hx = xf/2
    hy = yf/2
    s0 = f(x0, y0) + f(x0, yf) + f(xf, y0) + f(xf, yf)
    s1 = f(x0, hy) + f(hx, y0) + f(hx, yf) + f(xf, hy)
    s2 = f(hx, hy)
    
    return hx*hy/9 * (s0 + 4*s1 + 16*s2)
    
    
    
x0 = 0
y0 = 0
xf = 2
yf = 2
print(simp_sys(x0, y0, xf, yf))