#!/usr/bin/python
import sys

maxquantity = 0
maxdiscount = 0
current = None
revenue = None
for line in sys.stdin:
    line = line.strip()
    vals = line.split("\t")
    revenue = vals[0]
    values = vals[1].split("_")
    current_quant = int(values[0])
    current_dis = int(values[1])
    
    if current == revenue:
        if current_quant > maxquantity:
            maxquantity = current_quant
        if current_dis > maxdiscount:
            maxdiscount = current_dis
    else:
        if current != None:
            print '%s\t%s_%s' % (current, str(maxquantity), str(maxdiscount))
        current = revenue
        maxquantity = current_quant
        maxdiscount = current_dis
if current == revenue:
    print '%s\t%s_%s' % (current, str(maxquantity), str(maxdiscount))
            
            
