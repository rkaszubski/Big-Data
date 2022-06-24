#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    if line.endswith('res'):
        vals = line.split('\t')
        vals = vals[1].split('_')
        key = vals[2]
        brand = vals[0]
        revenue = vals[1]
        print key + '\t' + brand + "_" + revenue + "_" + "res"
    else:
        vals = line.split('|')
        season = vals[12]
        if season == "Fall":
            year = vals[4]
            key = vals[0]
            print key + '\t' + year + "_" + "date"

        
