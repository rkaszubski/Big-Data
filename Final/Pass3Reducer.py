#!/usr/bin/python

import sys

current = None
sumrev = 0
key = None

for line in sys.stdin:
    line = line.strip()
    vals = line.split("\t")
    key = vals[0]
    revenue = int(vals[1])

    if current == key:
        sumrev += revenue

    else:
        if current != None:
            print current + '\t' + str(sumrev)

        current = key
        sumrev = revenue
if current == key:
    print current + '\t' + str(sumrev)
