import math
import mwmath
import time

s = time.time()

def next_term(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

N = 1000001
max_length = 1
max_length_n = 1
chain_length_dict = {1:1}

ii = 2

while ii<N:
    cur_n = ii
    chain_length = 1
    while cur_n>1:
        cur_n = next_term(cur_n)

        if cur_n in chain_length_dict:
            chain_length+=chain_length_dict[cur_n]
            break
        
        chain_length+=1

    chain_length_dict[ii]=chain_length

    if chain_length>max_length:
        max_length = chain_length
        max_length_n = ii
        print "new length: "+str(chain_length)
    ii+=1
    
print max_length
print max_length_n

print time.time()-s
