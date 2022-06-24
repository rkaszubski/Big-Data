#!/usr/bin/python

import sys

numofpoints = 0
cluster = None
point1 = 0
point2 = 0
point3 = 0
point4 = 0
point5 = 0
point6 = 0

for line in sys.stdin:
    split = line.strip().split('\t')
    key = split[0]
    points = split[1].split(',')
    points = [int(i) for i in points]
    
    if cluster == key:
        point1 += points[0]
        point2 += points[1]
        point3 += points[2]
        point4 += points[3]
        point5 += points[4]
        point6 += points[5]
        numofpoints += 1
    else:
        if cluster:
            cent_1 = point1/numofpoints
            cent_2 = point2/numofpoints
            cent_3 = point3/numofpoints
            cent_4 = point4/numofpoints
            cent_5 = point5/numofpoints
            cent_6 = point6/numofpoints
            print cluster + '\t' + ','.join(map(str,[cent_1,cent_2,cent_3,cent_4,cent_5,cent_6]))
        
        point1 = points[0]
        point2 = points[1]
        point3 = points[2]
        point4 = points[3]
        point5 = points[4]
        point6 = points[5]
        cluster = key
        numofpoints = 1
cent_1 = point1/numofpoints
cent_2 = point2/numofpoints
cent_3 = point3/numofpoints
cent_4 = point4/numofpoints
cent_5 = point5/numofpoints
cent_6 = point6/numofpoints
print cluster + '\t' + ','.join(map(str,[cent_1,cent_2,cent_3,cent_4,cent_5,cent_6]))



        
