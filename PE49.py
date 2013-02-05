'''Project Euler #49

'''

import mwmath

prime_list = mwmath.build_n_digit_prime_list(4)

print len(prime_list)

potentials = []

for p in prime_list:
    p_prime_list = mwmath.build_prime_permutations_list(p)

    if p==min(p_prime_list):
        if len(p_prime_list)>2:
            potentials.append(p)

            for jj in range(len(p_prime_list)-1):
                diff = p_prime_list[jj+1]-p_prime_list[jj]

                if p_prime_list[jj]+diff in p_prime_list:
                    if p_prime_list[jj]+diff*2 in p_prime_list:
                        return str(p_prime_list[jj])+str(p_prime_list[jj]+diff)+str(p_prime_list[jj]+diff*2)
            
            
    else:
        continue
