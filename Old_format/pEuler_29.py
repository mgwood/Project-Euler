import math
import mwmath
import time

s = time.time()

ii=2
limit = 100
terms = {}

while ii<=limit:
    jj=2
    while jj<=limit:
        p = ii**jj
        if p in terms:
            terms[p]+=1
        else:
            terms[p]=1
        jj+=1
    ii+=1

print len(terms)

print time.time()-s
