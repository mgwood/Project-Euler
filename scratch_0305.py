'''Project Euler test
'''
import mwmath

p = []
ii = 100
while len(p)<50:
    p = mwmath.build_prime_list(ii)
    ii+=5

print p
