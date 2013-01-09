import math
import mwmath
import time

s = time.time()

N = 28123

abundant = []
odd_abundant = []

for ii in range(3,N):
    if mwmath.is_abundant(ii):
        abundant.append(ii)
        if (ii%2==1):
            odd_abundant.append(ii)
print time.time()-s
cur_sum = 0
for jj in range(N):
    #determine if each number can be written as the sum of abundants
    #1. make a sub-array of abundants<jj
    #2. for kk in sub-array, check if kk-jj in sub-array
    #3a. if yes, break.
    #3b. if not, check next kk
    #4. if all are checked w/o breaking, add jj to cur_sum
    if (jj%2==1):
        for mm in odd_abundant:
            if mm>jj:
                cur_sum+=jj
                break
            else:
                if (jj-mm) in abundant:
                    break
    else:
        for kk in abundant:
            if kk>jj:
                cur_sum+=jj
                break
            else:
                if (jj-kk) in abundant:
                    break

print cur_sum
print len(abundant)
print len(odd_abundant)

print time.time()-s
