'''Project Euler #55
'''

import mwmath
import time

def get_next_term(n,fact_dict):
    d = mwmath.get_digits(n)

    s = 0
    for ii in d:
        s+=fact_dict[ii]

    return s

def build_fact_chain(n,chain_dict,fact_dict):
    next_term = n
    chain = [next_term]
    while True:

        if chain_dict.has_key(next_term):
            chain_dict[n] = len(chain)+chain_dict[next_term]-1
            #for c in chain:
             #   chain_dict[c]=chain_dict[next_term]
                    
            return chain_dict[n]
        else:
            next_term = get_next_term(next_term,fact_dict)
            if next_term in chain[1::]:
                chain_dict[n] = len(chain)
  
                return chain_dict[n]
            else:
                chain.append(next_term)
            

def build_fact_dict():
    fact_dict = {}

    for ii in range(0,10):
        fact_dict[ii]=mwmath.nr_factorial(ii)

    return fact_dict

def main():
    fact_dict = build_fact_dict()
    chain_dict = {}

    count_60 = 0
    
    for ii in range(1,1000000):
        if build_fact_chain(ii,chain_dict,fact_dict)==60:
            count_60+=1

    return count_60

s = time.time()

fact_dict = build_fact_dict()
chain_dict = {}
print main()

print time.time()-s
