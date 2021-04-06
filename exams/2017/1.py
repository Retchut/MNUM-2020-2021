# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:05:08 2021

@author: Retch
"""

import math

k = 2.5

def F(x):
    return math.sqrt(k**2*math.exp(2*k*x)+1)

def trapezoid(x0, xf, h):
    
    n = round(abs(xf-x0)/h)
    
    s1 = 0
    for i in range(1, n):
        xi = x0 + i*h
        s1 += F(xi)
    
    return h/2 * (F(x0) + F(xf) + 2*s1)

def simpson(x0, xf, h):
    
    n = round(abs(xf-x0)/h)
    
    s1 = 0
    for i in range(1, n, 2):
        xi = x0 + i*h
        s1 += F(xi)
    
    s2 = 0
    for i in range(2, n-1, 2):
        xi = x0 + i*h
        s2 += F(xi)
    
    return h/3 * (F(x0) + F(xf) + 4*s1 + 2*s2)

def QC(s, s1, s2):
    return (s1-s)/(s2-s1)

def err(s1, s2, mo):
    return (s2-s1)/(2**mo -1)

a = 0
b = 1
h1 = 0.125
h2 = h1/2
h3 = h2/2

#trapezoid values:
t1 = trapezoid(a,b,h1)
t2 = trapezoid(a,b,h2)
t3 = trapezoid(a,b,h3)
#simpson values:
s1 = simpson(a,b,h1)
s2 = simpson(a,b,h2)
s3 = simpson(a,b,h3)

print("\t", "trapezoid", "\t\t\t\tsimpson")
print("h\t", h1, '\t\t\t\t\t', h1)
print("h'\t", h2, '\t\t\t\t',  h2)
print("h''\t", h3, '\t\t\t\t',  h3)
print("L1\t", t1, '\t',  s1)
print("L2\t", t2, '\t\t',  s2)
print("L3\t", t3, '\t\t',  s3)
print("QC\t", QC(t1, t2, t3), '\t\t', QC(s1, s2, s3))
print("err\t", err(t2, t3, 2), '\t', err(s2, s3, 4))


