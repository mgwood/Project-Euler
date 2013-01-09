import math
import mwmath
import time

s = time.time()

N_factors = 3

ii = 1
consecutive_N = 0

while consecutive_N<N_factors:
    factor_list = mwmath.find_prime_factors(ii)
    cur_factors = len(factor_list[0])

    if cur_factors==N_factors:
        consecutive_N+=1
    else:
        consecutive_N = 0

    ii+=1
    
print ii-N_factors

       
print time.time()-s
