#!/usr/bin/python

import sys

maxrev = 0
current = None
quantity = None
for line in sys.stdin:
    line = line.strip()
    vals = line.split("\t")

    quantity = int(vals[0])
    revenue = int(vals[1])

    if current == quantity:
        if revenue > maxrev:
            maxrev = revenue
    else:
        if current != None:
            print '%d\t%d' % (current, maxrev)
        current = quantity
        maxrev = revenue

if current == quantity:
    print '%d\t%d' % (current, maxrev)
            
        
