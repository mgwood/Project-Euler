import math
import mwmath
import time

s = time.time()

def get_common_digit(n1,n2):
    d1 = mwmath.get_digits(n1)
    d2 = mwmath.get_digits(n2)

    common = []
    
    for digit in d1:
        if digit in d2:
            common.append(digit)

    return common

def remove_common_digit(n1,n2,common):
    d1 = mwmath.get_digits(n1)
    d2 = mwmath.get_digits(n2)

    if d1[0]==common:
        new_1 = d1[1]
    else:
        new_1 = d1[0]

    if d2[0]==common:
        new_2 = d2[1]
    else:
        new_2 = d2[0]

    if new_2==0:
        return [1,0,0]
    else:
        return [new_1,new_2,1.0*new_1/new_2]

def check_fraction(n1,n2):
    d1 = mwmath.get_digits(n1)
    d2 = mwmath.get_digits(n2)
    if d1[1]==0:
        if d2[1]==0:
            return [1,1]
    
    init_frac = 1.0*n1/n2

    common = get_common_digit(n1,n2)
    if len(common)==0:
        return [1,1]
    
    [new_1,new_2,new_frac] = remove_common_digit(n1,n2,common[0])
    #print new_1
    #print new_2
    
    #print 'init:', init_frac
    #print 'new:', new_frac

    if init_frac==new_frac:
        print 'hit'
        print n1,' ',n2
        print new_1,' ',new_2
        return [new_1,new_2]
    else:
         return [1,1]

def main():

    total_num = 1
    total_den = 1

    for ii in range(10,100,1):
        for jj in range(10,ii,1):
            [n,d] = check_fraction(jj,ii)
            total_num = total_num*n
            total_den = total_den*d

    print 'total'
    print total_num,' ',total_den
    print 'lowest denom: ',t
    
main()
print time.time()-s
