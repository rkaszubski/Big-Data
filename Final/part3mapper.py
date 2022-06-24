#!/usr/bin/python
import sys
import numpy as np

f = open('centers.txt','r')

centers = f.readlines()
cents = {}
for center in range(0,len(centers)):
    cen = centers[center]
    cen = cen.strip('\n')
    cen = cen.split('\t')
    num = cen[0]
    points = cen[1].split(',')
    points = np.array([int(i) for i in points])
    cents[num] = points

for line in sys.stdin:
    line = line.strip()
    vals = line.split(',')
    vals = np.array([int(i) for i in vals])
    dist = 0
    cluster = 0
    for key in cents.keys():
        distance = np.linalg.norm(cents[key]-vals)
        if distance > dist:
            dist = distance
            cluster = key
    print str(cluster) + '\t' + ','.join(map(str,vals))
    


    
