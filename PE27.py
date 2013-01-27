'''Project Euler #27
'''
import mwmath
import time

def build_prime_list(n):
    
    potential_primes=[2,3]
    ii = 1
    while 6*ii<=(n):
        potential_primes.append(6*ii-1)
        potential_primes.append(6*ii+1)
        ii+=1

    prime_list=[]
    for jj in potential_primes:
        if mwmath.is_prime(jj):
            prime_list.append(jj)

    return prime_list

def check_consec_primes(a,b,prime_list):
    n = 0
    consec = 0
    next_term = n**2+a*n+b

    while next_term in prime_list:
        consec+=1
        n+=1
        next_term = n**2+a*n+b

    return consec
        
def max_consec_primes(n,limit):
    prime_list = build_prime_list(n)

    a = []

    for ii in prime_list:
        if ii<limit:
            a.append(ii)
            a.append(-1*ii)
        else:
            break
    b = a

    max_consec = 0
    max_consec_product = 0
    max_a = 0
    max_b = 0

    for jj in a:
        for kk in b:
            consec_terms = check_consec_primes(jj,kk,prime_list)
            if consec_terms>max_consec:
                max_consec=consec_terms
                max_consec_product = jj*kk
                max_a = jj
                max_b = kk

    return max_consec_product

def main():
    s = time.time()

    return [max_consec_primes(10000,1000),time.time()-s]
