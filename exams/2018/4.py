# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:15:00 2021

@author: Retch
"""

A=-7
B=4

def dyx(x, y, z): return z
def dzx(x, y, z): return A*z-B*y
def euler_sys(x0, y0, z0, h, n):
    
    x = x0
    y = y0
    z = z0
    
    print("x", "y", "y'")
    print(x, y, z)
    
    for i in range(n):
        dy = dyx(x,y,z) * h
        dz = dzx(x,y,z) * h
        x += h
        y += dy
        z += dz
        print(x, y, z)
    

h=0.2#0.8-0.6
x0 = 0.4#0.6 - h
y0 = 2.0
z0 = 1.0
n = 3

euler_sys(x0, y0, z0, h, n)
