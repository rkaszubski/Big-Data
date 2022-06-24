# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
a = np.matrix([[0,1,0,1],[0,0,1/2,0],[1/2,0,0,0],[1/2,0,1/2,0]])

vector = np.matrix([1/4,1/4,1/4,1/4]).T

for x in range(50):
    vector = a * vector
    print(vector)