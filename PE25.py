'''Project Euler #25
'''
import mwmath
import time


def find_first_N_length_fibb(N):

    ii=4

    fib_a = 1
    fib_b = 2
    while True:
        fib_c = fib_a+fib_b
        fib_count = mwmath.count_digits(fib_c)

        if fib_count==N:
            return ii
            break

        ii+=1
        fib_a = fib_b
        fib_b = fib_c

def main():
    s = time.time()

    return [find_first_N_length_fibb(1000),time.time()-s]
