import math

ii = 0

N = 100
sum = 0
sum_of_squares = 0

while ii<=N:
	sum+=ii
	sum_of_squares+=ii**2
	
	ii+=1
	
square_of_sum = sum**2

print square_of_sum-sum_of_squares