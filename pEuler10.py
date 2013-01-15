import math
import time

s = time.time()

def is_prime(n):
	prime = True
	
	if n==2 or n==3:
		return prime
	
	#candidate primes are of the form 6k+-1
	candidates = [2,3];
	ii = 1
	while ii*6<=(math.sqrt(n)+6):
		candidates.append(6*ii-1)
		candidates.append(6*ii+1)
		ii+=1
#	print candidates

	test=0
	while test<len(candidates):
		if n%candidates[test] == 0 and candidates[test]<n:
			prime = False
	
		test = test + 1
	
	return prime

sum = 2+3
candidates = [];
ii = 1
while ii*6<=2000000:
	candidates.append(6*ii-1)
	candidates.append(6*ii+1)
	ii+=1
#	print candidates

test=0
while test<len(candidates):
	if is_prime(candidates[test]):
		sum += candidates[test]
	
	test = test + 1

print sum
print time.time()-s