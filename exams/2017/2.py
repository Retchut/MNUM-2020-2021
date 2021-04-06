# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:06:53 2021

@author: Retch
"""

import math

def F(x, k):
    return math.sqrt( 1 + ( k*math.exp(k*x) )**2 )

def trap(x0, xf, k, h):
    
    n = round( (xf-x0)/h )
    res = F(x0, k) + F(xf, k)
    
    for i in range(1, n):
        res += 2*F(x0 + i*h, k)
    
    return h/2 * res


def simpson(x0,xf,k,h):
    
    n = round( (xf-x0)/h )
    res = F(x0, k) + F(xf, k)
    
    for i in range(1, n):
        if i%2 == 1:
            res += 4 * F(x0+i*h, k)
        elif i%2 == 0:
            res += 2 * F(x0+i*h, k)
    
    return h/3 * res

def QC(s0, s1, s2):
    return (s1-s0)/(s2-s1)

def err(mo, s1, s2):
    return (s2-s1)/(2**mo - 1)


k = 2.5
a=0
b=1
h0=0.125
h1=h0/2
h2=h1/2

#trapeze
t0 = trap(a, b, k, h0)
t1 = trap(a, b, k, h1)
t2 = trap(a, b, k, h2)
#simpson
s0 = simpson(a, b, k, h0)
s1 = simpson(a, b, k, h1)
s2 = simpson(a, b, k, h2)

print()
print("h:", h0, h1, h2)
print()
print("trap")
print("t0:", t0)
print("t1:", t1)
print("t2:", t2)
print("QC:", QC(t0,t1,t2))
print("err:", err(2, t1, t2))
print()
print("simpson")
print("s0:", s0)
print("s1:", s1)
print("s2:", s2)
print("QC:", QC(s0,s1,s2))
print("err:", err(4, s1, s2))