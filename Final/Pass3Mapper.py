#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    vals = line.split('\t')
    vals = vals[1].split('_')
    year = vals[0]
    brand = vals[1]
    revenue = vals[2]
    print year + '_' + brand + '\t' + revenue
    
