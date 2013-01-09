import math
import mwmath
import time

s = time.time()


n = 1000000
potential_primes = [2,3]
ii = 1
while 6*ii<=n:
    potential_primes.append(6*ii-1)
    potential_primes.append(6*ii+1)
    ii+=1

prime_list = []

for jj in potential_primes:
    if mwmath.is_prime(jj):
        prime_list.append(jj)

print time.time()-s

max_consec_primes = 1
prime_sum = 0
for kk in prime_list:
    prime_sum+=kk
    if prime_sum<=n:
        max_consec_primes+=1
    else:
        break
print max_consec_primes
limit = len(prime_list)
consec_primes = 2
max_consec = 1
max_prime = 2

while consec_primes<=max_consec_primes:
    mm = 0 #index in prime_list to check
    while mm<=(limit-consec_primes):
        if mm>=1 and (consec_primes%2==0):
            break
        else:
            consec_sum = sum(prime_list[mm:mm+consec_primes])
            if consec_sum>n:
                break
            if consec_sum in prime_list: #sum is prime
                max_consec = consec_primes
                max_prime = consec_sum

                break
        mm+=1
    consec_primes+=1

print max_consec
print max_prime

print time.time()-s
