# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:04:31 2021

@author: Retch
"""

import math

def F(x, k):
    return math.sqrt(1+ (k*math.exp(k*x))**2)

def df(x,k):
    return k*math.exp(k*x)

def trap(a0, b0, k, h):
    y0 = F(a0, k)
    yf = F(b0, k)
    s = 0
    steps = round((b0-a0)/h)
    
    for n in range(1, steps):
        xn = a0 + h*n
        s += F(xn, k)
        
    return h/2*(y0 + yf + 2*s)

def simp(a0, b0, k, h):
    y0 = F(a0, k)
    yf = F(b0, k)
    s1 = 0
    s2 = 0
    steps = round((b0-a0)/h)
    
    for n in range(1, steps, 2):
        xn = a0 + n*h
        s1 += F(xn, k)  
        
    for n in range(2, steps - 1, 2):
        xn = a0 + n*h
        s2 += F(xn, k)
        
    return h/3*(y0 + yf + 4*s1 + 2*s2)
    

def Qc(s0, s1, s2):
    return (s1-s0)/(s2-s1)

def err(s1, s2, o):
    return (s2-s1)/(2**o-1)

#common variables
k=1.5
a=0
b=2
h0=0.25
h1=h0/2
h2=h1/2

#for trapeze
ot = 2
lt0=trap(a, b, k, h0)
lt1=trap(a, b, k, h1)
lt2=trap(a, b, k, h2)

qt = Qc(lt0, lt1, lt2)
errt = err(lt1, lt2, ot)

#for simpson
os = 4
ls0=simp(a, b, k, h0)
ls1=simp(a, b, k, h1)
ls2=simp(a, b, k, h2)

qs = Qc(ls0, ls1, ls2)
errs = err(ls1, ls2, os)

print("Data\t\t Trapeze\t\t Simpson")
#print h, h' and h''
print("h\t\t\t" + str(h0) + '\t\t\t\t' + str(h0))
print("h'\t\t\t" + str(h1) + '\t\t\t\t' + str(h1))
print("h''\t\t\t" + str(h2) + '\t\t\t\t' + str(h2))

#print L, L' and L''
print("L\t\t\t" + str(lt0) + '\t' + str(ls0))
print("L'\t\t\t" + str(lt1) + '\t' + str(ls1))
print("L''\t\t\t" + str(lt2) + '\t' + str(ls2))

#print Qc and error
print("Qc\t\t\t" + str(qt) + '\t' + str(qs))
print("error\t\t" + str(errt) + '\t' + str(errs))