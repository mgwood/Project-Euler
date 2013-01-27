'''Project Euler #34

'''
import mwmath
import time

#has at most 7 digits
def main():
    s = time.time()
    
    fact_sum = []
    for ii in range(3,2903040):
        digits = mwmath.get_digits(ii)
        m_d = max(digits)
        if m_d<4 and ii>100:
            continue
        if m_d<6 and ii>10000:
            continue
        if m_d<9 and ii>1000000:
            continue
        if m_d<8 and ii>100000:
            continue
    
        if sum(map(mwmath.nr_factorial,digits))==ii:
            fact_sum.append(ii)

    return [sum(fact_sum),time.time()-s]
