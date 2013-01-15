import math
import mwmath
import time

s = time.time()

def n_pentagonal_numbers(n):
    pentagonal = []

    for ind in range(1,n+1):
        pentagonal.append(ind*(3*ind-1)/2)

    return pentagonal


pentagonal = n_pentagonal_numbers(10000)

s = time.time()

p_match = []
D = []
print 1560090 - 7042750
for p1 in pentagonal:
    for p2 in pentagonal:
        if p2<p1:
            continue
        else:
            if (p2+p1 in pentagonal):
                #print str(p1)+' + '+str(p2)
                if (p2-p1 in pentagonal):
                    print str(p1)+' - '+str(p2)
                    p_match.append(p1)
                    p_match.append(p2)
                    D.append(p2-p1)

print p_match
print D

print time.time()-s
