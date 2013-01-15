import math
import mwmath
import time

s = time.time()

limit = 10000

potential_primes_1 = [2,3]
ii = 1
while 6*ii<=limit:
    potential_primes_1.append(6*ii-1)
    potential_primes_1.append(6*ii+1)
    ii+=1

potential_primes_2 = [2,5]
print time.time()-s
for kk in potential_primes_1:
    if mwmath.is_prime(kk):
        potential_primes_2.append(kk)

jj = 9
check = True
while jj<limit and check:
    if jj in potential_primes_2:
        jj+=2
    else:
        for m in potential_primes_2:
            if m>jj:
                print jj
                check=False
                break
            else:
                diff = (jj-m)/2
                if mwmath.perfect_square(diff):
                    break
                

        jj+=2


print time.time()-s
