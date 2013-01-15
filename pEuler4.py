import math

def is_pal(n):
	n = str(n)
	palendrome = True

	ii = 0
	while ii<math.floor(len(n)/2):
		if n[ii]!=n[len(n)-1-ii]:
			palendrome = False
		
		ii = ii+1

	return palendrome


N = 1000
ii = 100
possible_pals = []


while ii<N:
	if is_pal(ii**2):
		possible_pals.append(ii**2)
	ii+=1
	
ii = 100
while ii<N:
	jj = 100
	while jj<N:
		if is_pal(ii*jj):
			possible_pals.append(ii*jj)
		jj+=1
	
	ii+=1
	
print possible_pals
print max(possible_pals)