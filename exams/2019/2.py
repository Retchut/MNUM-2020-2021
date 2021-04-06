# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:51:27 2021

@author: Retch
"""

def f1(x, y, a):
    return x**2-y-a

def df1x(x, y):
    return 2*x

def df1y(x, y):
    return -1

def f2(x, y, b):
    return -x+y**2-b

def df2x(x, y):
    return -1

def df2y(x, y):
    return 2*y

def sys_newton(x0, y0, a, b, n):
    x = x0
    y = y0
    print("iteration: 0\t xn = " + str(x) + "\t yn = " + str(y))
    for it in range(0, n):
        
        temp_x = x - ( f1(x, y, a)*df2y(x, y) - f2(x, y, b) * df1y(x, y) )/( df1x(x, y)*df2y(x,y) - df2x(x,y)*df1y(x,y))
        
        temp_y = y - ( f2(x,y,b)*df1x(x,y) - f1(x,y,a)*df2x(x,y) )/( df1x(x,y)*df2y(x,y) - df2x(x,y)*df1y(x,y) )
        
        x = temp_x
        y = temp_y
        
        print("iteration: " + str(it + 1) + "\t xn = " + str(x) + "\t yn = " + str(y))
        
a = 1.2
b = 1.0
x0 = 1.00000
y0 = 1.00000
n = 2
sys_newton(x0, y0, a, b, n)