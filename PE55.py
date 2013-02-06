'''Project Euler #55
'''

import mwmath

def reverse_and_add(n):
    m = int(str(n)[::-1])

    return m+n

def is_Lychrel(n):

    n_flips = 0

    while n_flips<51:

        n = reverse_and_add(n)
        n_flips+=1

        if mwmath.is_pal(n):
            return False

    return True

def main():
    
    L_count = 0

    for n in range(1,10000):
        if is_Lychrel(n):
            L_count+=1


    return L_count
