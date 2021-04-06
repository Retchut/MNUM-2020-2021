# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 01:29:56 2021

@author: Retch
"""
def Z(x,y):
    return 3*x**2-x*y+11*y+y**2-8*x

def dzx(x, y):
    return -y+6*y-8

def dzy(x, y):
    return 2*y-x+11

def grad(x0, y0, h, n):
    
    x = x0
    y = y0
    
    print("iteration 0")
    print("x=", str(x))
    print("y=", str(y))
    print("Z(x,y)=", str(Z(x,y)))
    print("gradX=", str(dzx(x, y)))
    print("gradY=", str(dzy(x, y)))
    print("lambda=", str(h))
    print()
    
    for i in range(0, n):
        
        temp_x = x - h * dzx(x,y)
        temp_y = y - h * dzy(x,y)
        
        if ( Z(temp_x, temp_y) < Z(x, y) ):
            x = temp_x
            y = temp_y
            print("iteration", str(i+1))
            print("x=", str(x))
            print("y=", str(y))
            print("Z(x,y)=", str(Z(x,y)))
            print("gradX=", str(dzx(x, y)))
            print("gradY=", str(dzy(x, y)))
            print("lambda=", str(h))
            print()
            h = 2*h
        elif ( Z(temp_x, temp_y) > Z(x, y) ):
            i = i-1
            h = h/2
        
    
    
    

x0 = 2
y0 = 2
h = 1
n = 1

grad(x0, y0, h, n)
    


