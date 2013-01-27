'''Project Euler #20
'''
import mwmath
import time

def main():
    s = time.time()
    
    return [sum(mwmath.get_digits(mwmath.nr_factorial(100))),time.time()-s]
