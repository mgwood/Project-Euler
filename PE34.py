'''Project Euler #34

'''
import itertools
import mwmath

def is_cube(n):
    return is_int(n**(1.0/3))

def is_int(n):
    return n==int(n)

lowest = int(4106325**(1.0/3))

print lowest
