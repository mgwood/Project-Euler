import math
import mwmath
import time

s = time.time()

print mwmath.is_pandigital(1234)
print mwmath.is_pandigital(12343)
print mwmath.is_pandigital(12)
print mwmath.is_pandigital(4312)

potential_primes = []
nn = 10000000
ii = 1000000
while 6*ii<=(nn):
    potential_primes.append(6*ii-1)
    potential_primes.append(6*ii+1)
    ii+=1

pan_list = []

for ele in potential_primes:
    if mwmath.is_pandigital(ele):
        if mwmath.is_prime(ele):
            pan_list.append(ele)
    
print pan_list

print time.time()-s
