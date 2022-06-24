#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    for num in range(0,9):
        if num == 6:
            swap = line[6].strip().split(' ')
            line[6] = swap[2] + "," + swap[1] + " " + swap[0]
        else:
            line[num] = line[num].replace(" ","_")
            line[num] = line[num].replace("#","_")
    print '\t'.join([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8]])
            
    
    
