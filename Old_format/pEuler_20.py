import math
import mwmath
import time

s = time.time()

def main():
    Fact = mwmath.nr_factorial(100)

    return sum(mwmath.get_digits(Fact))

print main()

print time.time()-s
