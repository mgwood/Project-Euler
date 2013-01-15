import math
import mwmath
import time

s = time.time()

def common_digits(n1,n2):
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

    for digit in d1:
        if not int(digit)==common:
            new_1 = float(digit)

    for digit2 in d2:

        if not int(digit2)==common:
            new_2 = float(digit2)
            if new_2==0:
                return [new_1,new_2,0]
    else:
        return [1,0,0]
            
    return [new_1,new_2,new_1/new_2]


def check_fraction(n1,n2):

    common = common_digits(n1,n2)
    f1 = float(n1)/float(n2)
    limit = float(10**(-5))
    
    if len(common)==0:
        return False
    if len(common)==1:
        if common[0]==0:
            return False
        f2 = remove_common_digit(n1,n2,common[0])[2]
        if abs(f1-f2)<limit:
            return True
    if len(common)==2:
        f2 = remove_common_digit(n1,n2,common[0])[2]
        f3 = remove_common_digit(n1,n2,common[1])[2]
        if abs(f1-f2)<limit:
            if common[0]==0:
                return False
            return True
        if abs(f1-f3)<limit:
            if common[1]==0:
                return False
            return True

    return False
        
example_N = []
example_D = []

for int1 in range(10,100):
    for int2 in range(int1,100):
        if check_fraction(int1,int2):
            example_N.append(int1)
            example_D.append(int2)
            print example_N
            print example_D

    if len(example_N)>=4:
        break

print check_fraction(49,98)

print example_N
print example_D

print time.time()-s
