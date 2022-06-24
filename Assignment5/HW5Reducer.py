#!/usr/bin/python

import sys

currentKey = None
valsEmp = []
valsCus = []
TotalCount = 0

for line in sys.stdin:

    split = line.strip().split('\t')
    key = split[0]
    value = split[1]
    
    if currentKey == key:
        if value.endswith('EMP'):
            valsEmp.append(value.split('_')[0])
        if value.endswith('CUS'):
            valsCus.append(value.split('_')[0])

    else:
        if currentKey:
            lenEmp = len(valsEmp)
            lenCus = len(valsCus)
            if (lenEmp*lenCus > 0):
                firstlast = currentKey
                for add in range(0,lenCus):
                    for ext in range(0,lenEmp):
                        print firstlast + '\t' + valsCus[add] + '_' + valsEmp[ext]
        valsEmp = []
        valsCus = []
        currentKey = key
        if value.endswith('EMP'):
            valsEmp.append(value.split('_')[0])
        if value.endswith('CUS'):
            valsCus.append(value.split('_')[0])

lenEmp = len(valsEmp)
lenCus = len(valsCus)
if (lenEmp*lenCus > 0):
    firstlast = currentKey
    for add in range(0,lenCus):
        for ext in range(0,lenEmp):
            print firstlast + '\t' + valsCus[add] + '_' + valsEmp[ext]
    
