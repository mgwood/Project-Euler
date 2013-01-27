'''Project Euler #32

'''
import mwmath
import time

def main():

    s = time.time()
    
    a_list = range(1,10000)
    b_list = range(100,10000)

    pan_list = []

    for a in a_list:
        for b in b_list:
            product = a*b
            p_length = mwmath.count_digits(product)+mwmath.count_digits(a)+mwmath.count_digits(b)

            if p_length<9:
                continue
            if p_length>9:
                break

            full_term = int(str(a)+str(b)+str(product))

            if mwmath.is_pandigital(full_term):
                if not product in pan_list:
                    pan_list.append(product)

    return [sum(pan_list),time.time()-s]

    
