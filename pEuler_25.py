import math
import mwmath
import time

s = time.time()

N = 1000
ii=4

fib_a = 1
fib_b = 2
while True:
    fib_c = fib_a+fib_b
    fib_count = mwmath.count_digits(fib_c)

    if fib_count==N:
        print ii
        print fib_c
        break

    ii+=1
    fib_a = fib_b
    fib_b = fib_c

print time.time()-s
