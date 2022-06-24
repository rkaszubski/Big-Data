#!/usr/bin/python
import random

f = open('numdata','w')

for row in range(0,360000):
    out = ''
    for num in range(0,10):
        if num < 9:
            out += str(random.randint(1,100))
            out += " "
        else:
            out += str(random.randint(1,100))
            out += "\n"
    f.write(out)

f.close()
