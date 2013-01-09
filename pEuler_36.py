import math
import mwmath
import time

s = time.time()

N = 1000000
cur_sum = 0

for ii in range(N):
    if (ii%2==1):
        if mwmath.is_pal(ii):
            b = str(bin(ii))
            if mwmath.is_pal(b[2:len(b)]):
                cur_sum+=ii

print cur_sum

print time.time()-s
