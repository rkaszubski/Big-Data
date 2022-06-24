#!/usr/bin/python
import sys

for line in sys.stdin:

    line = line.strip()
    split = line.split('|')

    if split[0].startswith('EMP'):
        key = split[1] + '_' + split[2]
        value = split[3] + '_' + 'EMP'
        print key + '\t' + value
    else:
        key = split[1] + '_' + split[2]
        value = split[3] + '_' + 'CUS'
        print key + '\t' + value

