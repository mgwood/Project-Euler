'''Project Euler #16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''
import mwmath

def digit_sum(n):
    return sum(mwmath.get_digits(n))

def main():
    return digit_sum(2**1000)
