''' Project Euler #63
'''

import itertools
import mwmath
import time
import math

count = 0

for t in range(1,1000):
    if 10**((t-1.0)/(t))>9:
        n_limit = t-1
        break

for n in range(1,n_limit+1):
    lower_lim = int(math.floor(10**((n-1.0)/(n))))
    upper_lim = 10

    for x in range(lower_lim,upper_lim):
        if mwmath.count_digits2(x**n)==n:
            count+=1

print count
