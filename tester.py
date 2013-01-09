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


new_p = 37

digits = mwmath.get_digits(new_p)
check = True
    
for digit in digits:
    if (digit%2==0):
        check=False
        print "Contains an even digit"
        

    #try to truncate from right
while check:
    if len(mwmath.get_digits(new_p))==1:
        break
    new_p = int(str(new_p)[1:])
    if not new_p in prime_list:
        print "Breaking "+str(new_p)+" is not prime"
        check=False

    #truncate from left
new_p = 37
while(check):
    if len(mwmath.get_digits(new_p))==1:
        break
    new_p = int(str(new_p)[:len(digits)-1])
    if not new_p in prime_list:
        print "Breaking "+str(new_p)+" is not prime"
        check=False

new_p = 37
if check:
    print "Found one: " +str(new_p)
    
print time.time()-s

