#!/usr/bin/python

import sys

currentKey = None
valsDate = []
valsRes = []

for line in sys.stdin:
    split = line.strip().split('\t')
    key = split[0]
    value = split[1]

    if currentKey == key:
        if value.endswith('date'):
            valsDate.append(value.split('_')[0])
        if value.endswith('res'):
            valsRes.append(value[:-4])
            
    else:
        if currentKey:
            lenDate = len(valsDate)
            lenRes = len(valsRes)
            #print lenDate, lenRes
            if (lenDate*lenRes >0):
                datekey = currentKey
                for year in range(0, lenDate):
                    for result in range(0,lenRes):
                        print datekey + '\t' + valsDate[year] + '_' + valsRes[result]

        valsDate = []
        valsRes = []
        currentKey = key
        if value.endswith('date'):
            valsDate.append(value.split('_')[0])
        if value.endswith('res'):
            valsRes.append(value[:-4])

lenDate = len(valsDate)
lenRes = len(valsRes)
if (lenDate*lenRes >0):
    datekey = currentKey
    for year in range(0, lenDate):
        for result in range(0,lenRes):
            print datekey + '\t' + valsDate[year] + '_' + valsRes[result]
