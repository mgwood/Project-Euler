'''Project Euler #36

'''
import mwmath
import time

def find_dec_bin_pal_sum(N):
    cur_sum = 0

    for ii in range(N):
        if (ii%2==1):
            if mwmath.is_pal(ii):
                b = str(bin(ii))
                if mwmath.is_pal(b[2:len(b)]):
                    cur_sum+=ii

    return cur_sum

def main():
    s = time.time()

    return [find_dec_bin_pal_sum(1000000),time.time()-s]
