#!/usr/bin/python

import sys

currentKey = None
valsPart = []
valsLOrev = []
valsLOdate = []
for line in sys.stdin:
    split = line.strip().split('\t')
    key = split[0]
    vals = split[1]

    if currentKey == key:
        if vals.endswith('part'):
            valsPart.append(vals.split('_')[0])
        if vals.endswith('lo'):
            valsLOrev.append(vals.split('_')[0])
            valsLOdate.append(vals.split('_')[1])
    else:
        if currentKey:
            lenPart = len(valsPart)
            lenLO = len(valsLOrev)
            if (lenPart * lenLO > 0):
                joinkey = currentKey
                for part in range(0,lenPart):
                    for lo in range(lenLO):
                        print joinkey + '\t' + valsPart[part] +'_' + valsLOrev[lo] +'_'+ valsLOdate[lo] +'_res'

        valsPart = []
        valsLOrev = []
        valsLOdate = []
        currentKey = key
        if vals.endswith('part'):
            valsPart.append(vals.split('_')[0])
        if vals.endswith('lo'):
            valsLOrev.append(vals.split('_')[0])
            valsLOdate.append(vals.split('_')[1])

lenPart = len(valsPart)
lenLO = len(valsLOrev)
if (lenPart * lenLO > 0):
    joinkey = currentKey
    for part in range(0,lenPart):
        for lo in range(lenLO):
            print joinkey + '\t' + valsPart[part] +'_' + valsLOrev[lo] +'_'+ valsLOdate[lo] + '_res'
