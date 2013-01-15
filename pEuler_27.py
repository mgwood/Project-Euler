import math
import mwmath
import time

s = time.time()

n = 10000
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


def check_consec_primes(a,b,prime_list):
    n = 0
    consec = 0
    next_term = n**2+a*n+b

    while next_term in prime_list:
        consec+=1
        n+=1
        next_term = n**2+a*n+b

    return consec
        
    
a = []

for ii in prime_list:
    if ii<1000:
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

print max_consec
print max_consec_product
print max_a
print max_b
print time.time()-s
