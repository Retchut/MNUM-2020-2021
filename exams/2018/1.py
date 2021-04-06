# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:17:52 2021

@author: Retch
"""

import math as m

def f1(x,y): return m.sin(x+y)-m.exp(x-y)
def f2(x,y): return m.cos(x+y)-(x**2)*(y**2)
def df1x(x,y): return m.cos(x+y)-m.exp(x-y)
def df1y(x,y): return m.cos(x+y)+m.exp(x-y)
def df2x(x,y): return -m.sin(x+y)-2*x*(y**2)
def df2y(x,y): return -m.sin(x+y)-2*(x**2)*y

def euler_sys(x, y, n):
    print("iteration 0", x,y)
    for i in range(n):
        kx = (f1(x,y)*df2y(x,y) - f2(x,y)*df1y(x,y))/(df1x(x,y)*df2y(x,y) - df2x(x,y)*df1y(x,y))
        ky = (f2(x,y)*df1x(x,y) - f1(x,y)*df2x(x,y))/(df1x(x,y)*df2y(x,y) - df2x(x,y)*df1y(x,y))
        x = x - kx
        y = y - ky
        print("iteration " + str(i+1), x,y)
    
    
x0 = 0.5
y0 = 0.25
n = 2

euler_sys(x0, y0, n)