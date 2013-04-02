'''Project Euler #53

'''
import mwmath
import time


def n_choose_r(n,r):
    fact1 = mwmath.nr_factorial(n)
    fact2 = mwmath.nr_factorial(r)
    fact3 = mwmath.nr_factorial(n-r)

    
    return fact1/(fact2*fact3)

def main():
    mil_count = 0

    for n in range(1,501):
        for r in range(1,n-1):
            a = n_choose_r(n,r)
            if a>1000000:
                mil_count+=1
                print a

    return mil_count

print main()

