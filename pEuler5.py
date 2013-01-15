import math

def is_prime(n):
	test = 2;
	prime = True
	
	if n==2:
		return prime

	while test<=math.sqrt(n):
		if n%test == 0:
			prime = False
	
		test = test + 1
	
	return prime
	
def LCM_n(n):
	product = 1;
	
	ii = 1
	while ii<=math.floor(n):
		if is_prime(ii):
			product*=ii
		
		if ii**2<=math.floor(n):
			product*=ii
		
		ii+=1
	
	return product

kk = 0
ii = 1
cur_prime = 0

while kk<10001:
	if is_prime(ii):
		cur_prime=ii
		kk+=1
	ii+=2
	
print cur_prime