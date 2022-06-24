#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    vals = line.split("|")
    #part tbl
    if vals[2].startswith("MFGR"):
        brand = vals[4]
        key = vals[0]
        brandnum = int(brand[5:])
        if brandnum >= 2121 and brandnum <= 2138:
            print key + '\t' + brand + '_' + "part"
    #lineorder tbl    
    else:
        key = vals[3]
        revenue = vals[12]
        orderdate = vals[5]
        print key + '\t' + revenue + '_' + orderdate + '_' + "lo"
