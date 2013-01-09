import math
import mwmath
import time

s = time.time()

#circular primes
#write a function to rotate digits

N = 1000000

c_prime_count = 0
c_primes = []

potential_primes_1 = [2,3]
ii = 1
while 6*ii<=(N):
    potential_primes_1.append(6*ii-1)
    potential_primes_1.append(6*ii+1)
    ii+=1

potential_primes_2 = [2,5]
print time.time()-s
for kk in potential_primes_1:
    if mwmath.circ_digit_check(kk) and mwmath.is_prime(kk):
        potential_primes_2.append(kk)

print time.time()-s

for jj in potential_primes_2:
    new_p = jj
    p_check = True
    rotations = mwmath.count_digits(jj)-1

    while p_check and rotations>0:
        new_p = mwmath.rotate_digits(new_p)
        p_check=mwmath.is_prime(new_p)

        rotations-=1
    if p_check:
        c_prime_count+=1
        c_primes.append(jj)

print c_prime_count
print c_primes

print time.time()-s
