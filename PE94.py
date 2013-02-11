''' Project Euler #94
'''

import mwmath

def almost_equilateral_area(a,b):
    h = (a**2-(0.5*b)**2)**(1.0/2)

    if is_int(h):
        return 2*a+b
    else:
        return 0
    
def is_int(n):
    return (int(n)==n)or(int(n)+1==n)


permimeter_limit = 1000000000
max_a = int(permimeter_limit/3)


permi_sum = 0

for ii in range(1,max_a+1):
    permi_sum+=almost_equilateral_area(ii,ii-1)
    permi_sum+=almost_equilateral_area(ii,ii+1)


print permi_sum
