import math
import mwmath
import time

s = time.time()

base_list = range(1,int(100000000/3))


largest_base = 1
largest_list = 1
largest_pan = 1

pan_list = []

for ele in base_list:
    cur_term = ele
    cur_product = 2

    while mwmath.count_digits(cur_term)<9:
        cur_term = int(str(cur_term)+str(cur_product*ele))
        cur_product+=1
        
    if mwmath.count_digits(cur_term)!=9:
        continue
    else:
        if mwmath.is_pandigital(cur_term):
            pan_list.append(cur_term)
            if cur_term>largest_pan:
                print cur_term
                largest_pan = cur_term
                largest_list = cur_product-1
                largest_base = ele

print pan_list
print largest_base
print largest_list
        

print time.time()-s
