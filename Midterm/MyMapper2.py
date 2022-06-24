#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    vals = line.split("\t")
    revenue = int(vals[0])
    values = vals[1].split("_")
    quantity = int(values[0])
    discount = int(values[1])

    if discount >= 4 and discount <= 8:
        print '%d\t%d' % (quantity, revenue)
