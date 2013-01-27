'''Project Euler #29

'''
import time

def a_b_powers(limit):
    

    ii=2
    terms = {}

    while ii<=limit:
        jj=2
        while jj<=limit:
            p = ii**jj
            if p in terms:
                terms[p]+=1
            else:
                terms[p]=1
            jj+=1
        ii+=1

    return len(terms)

def main():
    s = time.time()

    return [a_b_powers(100), time.time()-s]

