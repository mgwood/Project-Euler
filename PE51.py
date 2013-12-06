''' Project Euler #51
By replacing the 1st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the
ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
56773, and 56993. Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
'''

import time
import mwmath
import itertools
import re

s = time.time()

p_list = mwmath.build_n_digit_prime_list(5)

p_str = ''

for ele in p_list:
    p_str += str(ele)
    p_str += ' '


removed_digits = list(itertools.combinations(range(1, 5),2))

for prime in p_list:
    for ii in removed_digits:
        remaining_digits = ''

        for jj in range(0,4):
            if jj not in ii:
                remaining_digits+=str(prime)[jj]
            else:
                remaining_digits+='[0-9]'
    
        matches = len(re.findall(remaining_digits, p_str))

        print matches

        if matches==7:
            print prime
            break

        
    
