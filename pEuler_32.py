import math
import mwmath
import time

s = time.time()

tens_list = range(1,10000)
hundreds_list = range(100,10000)

pan_list = []

for ten in tens_list:
    for hundred in hundreds_list:
        product = ten*hundred
        p_length = mwmath.count_digits(product)+mwmath.count_digits(ten)+mwmath.count_digits(hundred)

        if p_length<9:
            continue
        if p_length>9:
            break

        full_term = int(str(ten)+str(hundred)+str(product))

        if mwmath.is_pandigital(full_term):
            print full_term
            if not product in pan_list:
                print product
                pan_list.append(product)

print sum(pan_list)
        

print time.time()-s
