import math
import time
import mwmath

s = time.time()

def is_terminating(n):
        if n==2 or n==5:
                return True
        if n%2==1 and n%5==1:
                return False
        
        prime_factors = mwmath.find_prime_factors(n)
        if (prime_factors[0] == [2]) or (prime_factors[0] == [5]) or (prime_factors[0] == [2,5]):
                return True
        else:
                return False

def mult_order_mod_n(a,n):
        k = 1
        while True:
                if a**k%n==1:
                        return k
                k+=1

potential_primes = []
ii = 1
while 6*ii<=(1000):
        potential_primes.append(6*ii-1)
        potential_primes.append(6*ii+1)
        ii+=1

primes = []
for p_ii in potential_primes:
        if mwmath.is_prime(p_ii):
                primes.append(p_ii)
primes.remove(5)
max_length = 1
max_p = 1

for p in primes:
        order = mult_order_mod_n(10,p)

        print str(p)+": "+str(order)
        
        if order>max_length:
                max_length = order
                max_p = p

print max_p
print max_length



print time.time()-s
