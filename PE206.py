'''Project Euler #206

'''
import mwmath
import time

def check_digit(n):
    checks = '1234567890'

    for ii in range(len(checks)):
        if not str(n)[2*ii]==checks[ii]:
            return False

    return True
        
def main():
    upper_lim = int((1929394959697989990)**(1.0/2))
    lower_lim = int((1020304050607080900)**(1.0/2))

    tries = range(lower_lim,upper_lim,10)

    for n in tries:
        if check_digit(n**2):
            return n


