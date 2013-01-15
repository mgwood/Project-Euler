import math
import time

s = time.time()

def perfect_square(n):
	if math.floor(math.sqrt(n))==n/math.sqrt(n):
		return True
	return False

def find_1000_triple(list_of_squares):
	triple = []
	product = 1
	jj = 0
	while jj<len(list_of_squares):
		kk = jj
		while kk<len(list_of_squares):
			if perfect_square(list_of_squares[jj]+list_of_squares[kk]):
				a = math.sqrt(list_of_squares[jj])
				b = math.sqrt(list_of_squares[kk])
				c = math.sqrt(list_of_squares[kk]+list_of_squares[jj])
				print a+b+c	
				if a+b+c==1000:
					triple.append(a)
					triple.append(b)
					triple.append(c)
					product = a*b*c
			kk+=1
		jj+=1
	
	print triple
	return product

list_of_squares = [];

ii = 1
while ii<1000000:
	if perfect_square(ii):
		list_of_squares.append(ii)
	ii+=1



print list_of_squares
print find_1000_triple(list_of_squares)
print time.time()-s