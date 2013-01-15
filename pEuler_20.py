import math
import mwmath
import time

s = time.time()

Fact = mwmath.nr_factorial(100)

digit_array = mwmath.get_digits(Fact)

sum = 0

for ii in digit_array:
    sum+=ii

print sum

print time.time()-s
