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

print get_common_digit(49,98)
print get_common_digit(49,99)



print time.time()-s
