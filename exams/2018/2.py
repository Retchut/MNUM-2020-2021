# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 23:24:36 2021

@author: Retch
"""

import math

def seidel(A, X, B):
    for i in range(0, 3):
        s1 = 0
        s2 = 0
        for j in range(0, 3):
            if j < i:
                s1 += A[i][j]# * X[i]
        
        for j in range(0,3):
            if j>i:
                s2 += A[i][j]#*X[j]
        
        X[i] = 1/A[i][i] * (-s1 - s2 + B[i])
    
    print("xn+1 = ", str(X[0]))
    print("yn+1 = ", str(X[1]))
    print("zn+1 = ", str(X[2]))
    

A=[[1, 5.5, 3], [103, 60, 41], [2, 10, 13]]
B=[0, 1.2, -13]
X=[0,0,0]

seidel(A,X,B)