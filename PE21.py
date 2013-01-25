'''Project Euler #21

'''
import mwmath
#Plan:
#1. write sumOfFactors in mwmath
#2. build dictionary where key=n and val=sumOfFactors(n)
#3. searh dict to find when dict[key]=key
def build_factor_dict(N):
    factor_dict = {}

    for ii in range(1,N+1):
        factor_dict[ii]=mwmath.sumOfFactors(ii)

    return factor_dict

def find_amicable_sum(N):

    factor_dict = build_factor_dict(N)

    amicable_sum = 0
    jj = 1
    kk = 1
    while jj<N:
        key_1 = jj
        val_1 = factor_dict[jj]
        kk=jj+1
        while kk<N:
            key_2 = kk
            val_2 = factor_dict[kk]

            if key_1==val_2 and val_1==key_2:
                amicable_sum+=jj+kk
        
            kk+=1

        jj+=1
    return amicable_sum

def main():
    return find_amicable_sum(10000)
print main()
