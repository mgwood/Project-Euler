''' Project Euler #60
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and
concatenating them in any order the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate
to produce another prime.
'''

import time
import mwmath
import re

s = time.time()

p_list = mwmath.build_prime_list(10000)

print time.time()-s
t = time.time()

for p_1 in p_list:
    for p_2 in p_list:
        if p_2<=p_1:
            continue
        if not mwmath.concat_prime_list(p_2,[p_1],p_list):
            continue
        for p_3 in p_list:
            if p_3<=p_1:
                continue
            if p_3<=p_2:
                continue
            if not mwmath.concat_prime_list(p_3,[p_1,p_2],p_list):
                continue
            for p_4 in p_list:
                if p_4<=p_1:
                    continue
                if p_4<=p_2:
                    continue
                if p_4<=p_3:
                    continue
                if not mwmath.concat_prime_list(p_4,[p_1,p_2,p_3],p_list):
                    continue
                for p_5 in p_list:
                    if p_5<=p_1:
                        continue
                    if p_5<=p_2:
                        continue
                    if p_5<=p_3:
                        continue
                    if p_5<=p_4:
                        continue


                    if mwmath.concat_prime_list(p_5,[p_1,p_2,p_3,p_4],p_list):
                        print [p_1,p_2,p_3,p_4,p_5]
                        print p_1+p_2+p_3+p_4+p_5

else:
    print 'None found'



print time.time()-t
