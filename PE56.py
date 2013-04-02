'''Project Euler #53

'''
import mwmath
import time

m_sum = 0
m = 0

for a in range(90,100):
    for b in range(90,100):
        n = a**b
        cur = mwmath.digit_sum(n)
        if cur>m_sum:
            m_sum = cur
            m = n

print m
print m_sum
        
