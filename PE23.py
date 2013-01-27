'''Project Euler #23

'''
import mwmath
import time


def build_abundant_list(N):
    abundant = []
    odd_abundant = []

    for ii in range(3,N):
        if mwmath.is_abundant(ii):
            abundant.append(ii)
            if (ii%2==1):
                odd_abundant.append(ii)

    return [abundant, odd_abundant]

def calc_abundant_sum(N):    
    abundant_list = build_abundant_list(N)
    abundant = abundant_list[0]
    odd_abundant = abundant_list[1]

    cur_sum = 0
    for jj in range(N):
        #determine if each number can be written as the sum of abundants
        #1. make a sub-array of abundants<jj
        #2. for kk in sub-array, check if kk-jj in sub-array
        #3a. if yes, break.
        #3b. if not, check next kk
        #4. if all are checked w/o breaking, add jj to cur_sum
        if (jj%2==1):
            for mm in odd_abundant:
                if mm>jj:
                    cur_sum+=jj
                    break
                else:
                    if (jj-mm) in abundant:
                        break
        else:
            for kk in abundant:
                if kk>jj:
                    cur_sum+=jj
                    break
                else:
                    if (jj-kk) in abundant:
                        break

    return cur_sum

def main():
    s = time.time()

    return [calc_abundant_sum(28123),time.time()-s]
