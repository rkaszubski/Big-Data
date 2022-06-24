#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    newdate = str(line[7]) + '/' + str(line[8]) + '/' + str(line[9])
    print '\t'.join([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[10],line[12],line[13],line[15],line[16],newdate])
    
