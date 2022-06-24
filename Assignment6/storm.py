#!/usr/bin/python

import sys

window = int(sys.argv[1])
move = int(sys.argv[2])
vals = []

for line in sys.stdin:
    vals.append(int(line))
    if len(vals) == window:
        total = 0
        #print vals
        for item in vals:
            total += item
        average = total/float(window)
        print average
        vals = vals[-(window-move):]


