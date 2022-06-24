#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    vals = line.split("|")
    quantity = int(vals[8])
    if quantity >= 17 and quantity <= 24:
        print '%s\t%s' % (vals[16], vals[14])
