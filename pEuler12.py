import math
import time

def is_prime(n):
        n = math.floor(n)
        prime = True

        if n==2 or n==3:
                return prime
        
        potential_primes = [2,3]
        ii = 1
        while 6*ii<=(n):
                potential_primes.append(6*ii-1)
                potential_primes.append(6*ii+1)
                ii+=1

        jj = 0
        limit = len(potential_primes)
        while jj<limit:
                if n%potential_primes[jj] == 0 and potential_primes[jj]<n:
                        prime = False
                jj+=1
        
        return prime

def find_prime_factors(n):
        n = math.floor(n)        
        potential_primes = [2,3]
        ii = 1
        lim_1 = math.sqrt(n+6)
        while 6*ii<=lim_1:
                potential_primes.append(6*ii-1)
                potential_primes.append(6*ii+1)
                ii+=1

        jj = 0
        limit = len(potential_primes)
        prime_factors = [];
        factor_count = [];
        while jj<limit:
                if n%potential_primes[jj] == 0:
                        if is_prime(potential_primes[jj]):
                                prime_factors.append(potential_primes[jj])
                                factor_count.append(1)
                                new_div = n
                                while (new_div/potential_primes[jj])%potential_primes[jj]==0:
                                        factor_count[-1]+=1
                                        new_div = new_div/potential_primes[jj]
                jj+=1
        
        return [prime_factors,factor_count]

def find_factors(n):
        n = math.floor(n)

        factors = [1]

        ii = 2
        while ii<=n:
                if n%ii==0:
                        factors.append(ii)
                ii+=1
        return factors

def count_factors(n):
        n = math.floor(n)
        prime_factorization = find_prime_factors(n)

        factor_count = 1

        ii = 0
        limit = len(prime_factorization[1])

        while ii<limit:
                factor_count*=(prime_factorization[1][ii]+1)
                ii+=1

        return factor_count

        
s = time.time()


N_factors_limit = 500
ii = 2
prev_triangle = 1
two_limit = 2^(N_factors_limit-2)
while True:
        prev_triangle = prev_triangle+ii
        if prev_triangle%2==1 or prev_triangle<two_limit:
                ii+=1
        else:
                count = count_factors(prev_triangle)
                if count>N_factors_limit:
                        print ii
                        print prev_triangle
                        break    
                ii+=1


print time.time()-s
