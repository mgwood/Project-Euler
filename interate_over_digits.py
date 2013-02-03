import math
import time



a = 1242342424132546757345435435345345353453537584758742579
d = []

#all numerical
s = time.time()
for ii in range(int(math.log10(a)),-1,-1):
    d.append(int(a/10**ii)%(10))
print time.time()-s

#hybrid str/numerical
s = time.time()
for ii in range(len(str(a))-1,-1,-1):
    d.append(int(a/10**ii)%(10))
print time.time()-s

#all str
d = []
s = time.time()
for ii in str(a):
    d.append(int(ii))
print time.time()-s
