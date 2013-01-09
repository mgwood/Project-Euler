import math
import mwmath
import time

s = time.time()


n = 100
potential_primes = [2,3]
ii = 1
while 6*ii<=n
    potential_primes.append(6*ii-1)
    potential_primes.append(6*ii+1)
    ii+=1

prime_list = []

for jj in potential_primes
    if mwmath.is_prime(jj):
        prime_list.append(jj)

print prime_list

print time.time()-s
