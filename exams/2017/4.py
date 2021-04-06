# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:07:02 2021

@author: Retch
"""

import math

a = 30
b = 0.5

def dCt(t, C, T):
    return - math.exp(-b / (T + 273)) * C

def dTt(t, C, T):
    return a * math.exp(-b / (T + 273)) * C - b * (T-20)

def euler_sys(t0, dt, C0, T0, n):
    '''
    print()
    print("euler")
    print("it t C T")
    print(0, t0, C0, T0)'''
    
    for i in range(n):
        dC = dCt(t0, C0, T0) * dt
        dT = dTt(t0, C0, T0) * dt
        
        t0 += dt
        C0 += dC
        T0 += dT
        
        #print(i+1, t0, C0, T0)
        
    return [t0, C0, T0]
        
def rk4(x0, dx, y0, z0, n, dyx, dzx):
    '''
    print()
    print("rk4")
    print("it t C T")
    print(0, x0, y0, z0)'''
    
    for i in range(n):
        del1y = dx * dyx(x0, y0, z0)
        del1z = dx * dzx(x0, y0, z0)
        
        del2y = dx * dyx(x0 + dx/2, y0 + del1y/2, z0 + del1z/2)
        del2z = dx * dzx(x0 + dx/2, y0 + del1y/2, z0 + del1z/2)
        
        del3y = dx * dyx(x0 + dx/2, y0 + del2y/2, z0 + del2z/2)
        del3z = dx * dzx(x0 + dx/2, y0 + del2y/2, z0 + del2z/2)
        
        del4y = dx * dyx(x0 + dx, y0 + del3y, z0 + del3z)
        del4z = dx * dzx(x0 + dx, y0 + del3y, z0 + del3z)
        
        dy = del1y/6 + del2y/3 + del3y/3 + del4y/6
        dz = del1z/6 + del2z/3 + del3z/3 + del4z/6
        
        x0 += dx
        y0 += dy
        z0 += dz
        
        #print(i+1, x0, y0, z0)
        
    return [x0, y0, z0]
        
def QC(s0, s1, s2):
    return (s1-s0)/(s2-s1)

def err(mo, s1, s2):
    return (s2-s1)/(2**mo - 1)

t0 = 0
dt = 0.5 / 2
C0 = 2.5
T0 = 25
n = 2
'''
#a)
euler_sys(t0, dt, C0, T0, n)

#b)
rk4(t0, dt, C0, T0, n, dCt, dTt)
'''
#c)
dt1 = dt/2
dt2 = dt1/2
s0 = euler_sys(t0, dt, C0, T0, n)
n1 = n*2
s1 = euler_sys(t0, dt1, C0, T0, n1)
n2 = n1*2
s2 = euler_sys(t0, dt2, C0, T0, n2)

T0 = s0[2]
T1 = s1[2]
T2 = s2[2]

print("hs:", dt1, dt2)
print("Ts:", T1, T2)
print("euler temperature QC and error")
print(QC(T0, T1, T2))
print(err(1, T1, T2))

