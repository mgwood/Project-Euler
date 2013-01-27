'''Project Euler #35

'''

import mwmath
import time

#circular primes
#write a function to rotate digits

def find_circ_primes(N):

    c_primes = []

    potential_primes_1 = [2,3]
    ii = 1
    while 6*ii<=(N):
        potential_primes_1.append(6*ii-1)
        potential_primes_1.append(6*ii+1)
        ii+=1

    potential_primes_2 = [2,5]
    for kk in potential_primes_1:
        if mwmath.circ_digit_check(kk) and mwmath.is_prime(kk):
            potential_primes_2.append(kk)


    for jj in potential_primes_2:
        new_p = jj
        p_check = True
        rotations = mwmath.count_digits(jj)-1

        while p_check and rotations>0:
            new_p = mwmath.rotate_digits(new_p)
            p_check=mwmath.is_prime(new_p)

            rotations-=1
        if p_check:
            c_primes.append(jj)

    return c_primes


def main():
    s = time.time()

    return [len(find_circ_primes(1000000)),time.time()-s]

    
