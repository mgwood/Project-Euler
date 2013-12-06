'''Project Euler #58

'''
import mwmath
import time

def main():
    t = time.time()
    cf_list = mwmath.build_sqrt2_continued_fraction_terms(999)
    print time.time()-t
    
    count = 0;
    #print cf_list
    for ii in cf_list:
        act_term = mwmath.get_actual_sqrt2_cf(ii[0],ii[1])
        if mwmath.count_digits(act_term[0])>mwmath.count_digits(act_term[1]):
            #print act_term
            count = count + 1

    print time.time()-t
    return count

print main()
