import math
import mwmath
import time

s = time.time()

def expected_value(ratio,flips,success,failure):
    P_row=mwmath.pascal_row(flips)
    denom = 2**flips
    expected_val = 0

    for ii in range(flips+1):
        ratio = P_row[ii]/denom
        expected_val+=(ratio*((success)**(flips-ii))*((failure)**(ii)))

    return expected_val

def count_wins(ratio,flips,success,failure,limit):
    P_row=mwmath.pascal_row(flips)
    above_limit = 0.0
    
    for ii in range(flips+1):

        #s = long(success)
        #if (s)**(flips-ii)>=limit:
        #    above_limit+=P_row[ii]
        #    continue
        
        new_val=(((success)**(flips-ii))*((failure)**(ii)))
        if new_val>=limit:
            above_limit+=P_row[ii]

    return above_limit

flips = 300
N = range(1,5000)
max_count = 0
max_count_N = 1
limit=1000

for ii in N:
    ratio = 1.0/(ii/1000.0)
    if ratio>=1:
        continue
    success = (1+2*ratio)
    failure = (1-ratio)

    new_count = count_wins(ratio,flips,success,failure,limit)

    if new_count>max_count:
        max_count = new_count
        max_count_N = ii

print max_count
print max_count_N
print 1.0/max_count_N

print time.time()-s
