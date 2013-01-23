import math
import mwmath
import time

s = time.time()

N = 20
ways = 2*N*1+mwmath.get_triangle_n(N-1)*2

print ways

print time.time()-s
