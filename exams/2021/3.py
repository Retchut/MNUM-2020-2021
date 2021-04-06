# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:05:05 2021

@author: Retch
"""


def gauss_seidel(A, B, X, lines, cols):
    
    X0 = X
    
    for i in range(lines):
        
        s1 = 0
        for j in range(cols):
            if j < i:
                s1 += A[i][j] * X[j]
                
        s2 = 0
        for j in range(cols):
            if j > i:
                s2 += A[i][j]*X0[j]
            
        X[i] = 1/A[i][i] * (-s1 - s2 + B[i])
        
    
    print("x1:")
    for i in range(lines):
        print(X[i])
    

A = [[6.0, 0.5, 3.0, 0.25], [1.2, 3.0, 0.25, 0.2], [-1.0, 0.25, 4.0, 2.0], [2.0, 4.0, 1.0, 8.0]]
B = [19.0, -2.2, 9.0, 15.0]
x0 = [3.16667, -2.0, 3.16667, 1.68750]
lines = len(A)
cols = len(A[0])

gauss_seidel(A, B, x0, lines, cols)