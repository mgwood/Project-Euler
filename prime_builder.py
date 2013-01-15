import math
import mwmath
import time

s = time.time()

N = 100000000

potential_primes = [2,3]
ii = 1
while 6*ii<=(N):
    potential_primes.append(6*ii-1)
    potential_primes.append(6*ii+1)
    ii+=1

w_file = open("primes_to_100000000.txt","w")

for ele in potential_primes:
    if mwmath.is_prime(ele):
        w_file.write(str(ele)+"\n")

w_file.close()


r_file = open("primes_to_100000s000.txt","r")

def check_prime(n,f):
    return str(n) in f.read()

s = time.time()
print check_prime(5,r_file)
print check_prime(51,r_file)
print check_prime(53234239,r_file)

r_file.close()

print time.time()-s

s = time.time()
print mwmath.is_prime(5)
print mwmath.is_prime(51)
print mwmath.is_prime(53234239)

print time.time()-s
