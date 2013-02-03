import math
import time



a = 1242342424132546757345435435345345353453537584758742579
d = []

s = time.time()
for ii in range(int(math.log10(a)),-1,-1):
    d.append(int(a/10**ii)%(10))
print time.time()-s

d = []
s = time.time()
for ii in str(a):
    d.append(int(ii))
print time.time()-s
