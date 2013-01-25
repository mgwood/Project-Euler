import math
import mwmath
import time

s = time.time()

#Plan:
#1. write sumOfFactors in mwmath
#2. build dictionary where key=n and val=sumOfFactors(n)
#3. searh dict to find when dict[key]=key

def find_amicable_sum(N):
    
    dict_factor = {}
    ii = 1

    while ii<N:
        dict_factor[ii]=mwmath.sumOfFactors(ii)
        ii+=1

    amicable = []
    jj = 1
    kk = 1
    while jj<N:
        key_1 = jj
        val_1 = dict_factor[jj]
        kk=jj+1
        while kk<N:
            key_2 = kk
            val_2 = dict_factor[kk]

            if key_1==val_2 and val_1==key_2:
                amicable.append(jj)
                amicable.append(kk)
        
            kk+=1

        jj+=1

    return sum(amicable)

def main():
    return find_amicable_sum(10000)

print main()

print time.time()-s
