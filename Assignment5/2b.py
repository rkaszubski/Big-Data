# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 17:06:50 2021

@author: rober
"""
#A X Z Q P
import numpy as np
a = np.matrix([[0,1/2,1/3,0,0],[0,0,1/3,0,0],[1,0,0,0,0],[0,1/2,1/3,0,0],[0,0,0,1,0]])

vector = np.matrix([1/5,1/5,1/5,1/5,1/5]).T
print(a)
print(vector)
for x in range(2540):
    vector = a * vector
    print(vector)