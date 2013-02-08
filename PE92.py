'''Project Euler #55
'''

import mwmath
import time

def get_next_term(n):
    d = mwmath.get_digits(n)

    s = 0
    for ii in d:
        s+=ii**2

    return s

def arrives_at_89(n,chain_dict):
    next_term = n
    chain = [next_term]
    while True:
        #if next_term==1:
         #   chain_dict[n] = False

          #  for c in chain:
           #     chain_dict[c]=False
            
            #return chain_dict[n]
        #if next_term==89:
         #   chain_dict[n] = True
          #  for c in chain:
           #     chain_dict[c]=True
                    
            #return chain_dict[n]
        
        if chain_dict.has_key(next_term):
            chain_dict[n] = chain_dict[next_term]
            for c in chain:
                chain_dict[c]=chain_dict[next_term]
                    
            return chain_dict[n]
        else:
            next_term = get_next_term(next_term)
            chain.append(next_term)
            

def main():
    chain_dict = {1:False,89:True}

    count_89 = 0
    
    for ii in range(1,10000001):
        if arrives_at_89(ii,chain_dict):
            count_89+=1

    return count_89

s = time.time()

print main()

print time.time()-s
