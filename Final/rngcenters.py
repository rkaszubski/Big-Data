#/usr/bin/python

import random
f = open('part3data','r')

data = f.readlines()
f.close()
rngpoints = random.sample(range(0,2100000),4)
f = open('centers.txt','w')
count = 1
for point in rngpoints:
    f.write("{}\t{}".format(count,data[point]))
    count += 1
f.close()
