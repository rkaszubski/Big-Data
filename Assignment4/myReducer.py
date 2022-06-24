#!/usr/bin/python

import sys
import statistics    

dev =[]
current = None
shipmode = None
for line in sys.stdin:
    line = line.strip()
    vals = line.split("\t")
    shipmode = vals[0]
    
    if current == shipmode:
        dev.append(int(vals[1]))
    else:
        if current != None:
            print '%s\t%f' % (current, statistics.stdev(dev)) 
        current = shipmode
        dev = [int(vals[1])]

if current == shipmode:
    print '%s\t%f' % (current, statistics.stdev(dev))
