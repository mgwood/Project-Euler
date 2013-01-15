import math
import mwmath
import time

s = time.time()

#has at most 7 digits


fact_sum = []


for ii in range(3,2903040):
    digits = mwmath.get_digits(ii)
    m_d = max(digits)
    if m_d<4 and ii>100:
        continue
    if m_d<6 and ii>10000:
        continue
    if m_d<9 and ii>1000000:
        continue
    if m_d<8 and ii>100000:
        continue
    
    if sum(map(mwmath.nr_factorial,digits))==ii:
        fact_sum.append(ii)

print fact_sum
print sum(fact_sum)

print time.time()-s
