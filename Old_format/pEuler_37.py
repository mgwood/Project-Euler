'''Project Euler #37

'''

import mwmath
import time

def find_truncatable_primes(prime_list):

    truncatable_count = 0
    trunc_sum = 0
    kk = 0
    while truncatable_count<11:
        new_p = prime_list[kk]
        if new_p<11:
            kk+=1
            continue

        digits = mwmath.get_digits(new_p)
        check = True

        if digits[0]==1 or digits[0]==9:
            check=False
        if new_p%10==1 or new_p%10==9:
            check=False
        for digit in digits:
            if (digit!=2) and (digit%2==0):
                check=False

        #try to truncate from rinth
        while check:
            if len(mwmath.get_digits(new_p))==1:
                break
            new_p = int(str(new_p)[1:])
            if not new_p in prime_list:
                check=False
    
        #truncate from left
        new_p = prime_list[kk]
        while check:
            if len(mwmath.get_digits(new_p))==1:
                break
            new_p = int(str(new_p)[:len(mwmath.get_digits(new_p))-1])
            if not new_p in prime_list:
                check=False

        new_p = prime_list[kk]
        if check:
            truncatable_count+=1
            trunc_sum+=new_p
            print "Found one: " +str(new_p)
    
        kk+=1

    return trunc_sum

def main():
    s = time.time()
        
    return [find_truncatable_primes(mwmath.build_prime_list(1000000)),time.time()-s]
