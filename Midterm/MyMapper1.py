#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    vals = line.split('|')
    orderpriority = vals[6]
    if orderpriority.endswith("URGENT"):
        print '%s\t%s_%s' % (vals[12], vals[8], vals[11])
