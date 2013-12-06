'''Project Euler #66

'''

import mwmath
import math
import time

def sold_quad_Dio(D,limit):

    x_range_min = 2
    x_range_max = limit/100000

    while True:
        for ii in range(x_range_min,x_range_max+1):
            A = pow(ii,2)
            for jj in range(1,ii+1):
                
                if A-D*pow(jj,2)==1:
                    return [ii,jj]

        x_range_min = x_range_max
        x_range_max = x_range_max*2
        
        if x_range_min>limit:
            return [1,1]


def sold_quad_Dio_2(D,limit):

    x_range_min = 2
    x_range_max = limit/10

    while True:
        for ii in range(x_range_min,x_range_max+1):
            A = pow(ii,2)
            #print A
            t = (A-1.0)/D
            #print t
            if mwmath.perfect_square(t):
                #print ii
                return [ii]
        x_range_min = x_range_max
        x_range_max = x_range_max*2
        if x_range_min>limit:
            print 'hit limit'
            return [1,1]
'''
print 'Next up: 3'
sold_quad_Dio_2(3,100)
print 'Next up: 5'
sold_quad_Dio_2(5,100)
print 'Next up: 6'
sold_quad_Dio_2(6,100)
print 'Next up: 7'
sold_quad_Dio_2(7,100)
print 'Next up: 13'
sold_quad_Dio_2(13,1000)
'''
def main(N1,N2):
    max_x = 1
    max_D = 1

    for ii in range(N1,N2+1):
        if not mwmath.is_prime(ii):
            continue
        else:
            temp = sold_quad_Dio_2(ii,ii*10000000)
            #print temp
            if temp[0]>max_x:
                max_x = temp[0]
                max_D = ii

    return max_D

t = time.time()
print main(900,1000)
print time.time()-t
