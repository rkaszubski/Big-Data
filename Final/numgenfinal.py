#/usr/bin/python
import random

for row in range(0,2100000):
    columns = random.sample(range(1,101),6)
    print ','.join(map(str,columns))
