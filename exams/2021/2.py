# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:44:02 2021

@author: Retch
"""

import math

#sendo h = 4, h' = 2 e h'' = 1
#F=[0, 0.15, 0.3, 0.45, 0.60, 0.75, 0.90, 1.05, 1.20]
#a=[0, 0.03, 0.07, 0.10, 0.13, 0.17, 0.20, 0.23, 0.26]
F = [0.0, 0.30, 0.60, 0.90, 1.20, 1.50, 1.80, 2.1, 2.4]
a = [0.0, 0.07, 0.13, 0.20, 0.26, 0.33, 0.40, 0.46, 0.53]

def Fint(x):
    return F[x]*math.cos(a[x])

def trap(x0, xf, h):
    n = round(abs(xf-x0)/h)
    
    res = Fint(x0) + Fint(xf)
    
    for i in range(1, n):
        res += 2*Fint(round(x0 + i*h))
        
    return 2 * math.pi * h/2 * res


def simpson(x0, xf, h):
    n = round(abs(xf-x0)/h)
    
    res = Fint(x0) + Fint(xf)
    
    for i in range(1, n):
        if i%2 == 1:
            res += 4*Fint(round(x0 + i*h))
        elif i%2 == 0:
            res += 2*Fint(round(x0 + i*h))
        
        
    return 2* math.pi * h/3 * res

def QC(s, s1, s2):
    return (s1-s)/(s2-s1)

def err(s1, s2, mo):
    return (s2-s1)/(2**mo -1)

h = 4
h1 = h/2
h2 = h1/2

x0 = 0
xf = 8

#trap values:
t0 = trap(x0,xf,h)
t1 = trap(x0,xf,h1)
t2 = trap(x0,xf,h2)

#simpson values:
s0 = simpson(x0,xf,h)
s1 = simpson(x0,xf,h1)
s2 = simpson(x0,xf,h2)


print("h:\t", h)
print("h':\t", h1)
print("h'':", h2)
print()
print("\t", "trap")
print("L1:\t", t0)
print("L2:\t", t1)
print("L3:\t", t2)

print("QC:\t", QC(t0, t1, t2))
print("err:", err(t1, t2, 2))
print()
print("\t", "simpson")
print("L1:\t", s0)
print("L2:\t", s1)
print("L3:\t", s2)
print("QC:\t", QC(s0, s1, s2))
print("err:", err(s1, s2, 4))