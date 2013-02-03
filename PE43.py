''' Project Euler #11
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
import mwmath
import itertools

def check_substring_properties(n):
    digits = mwmath.get_digits(n)

    prime_list = [2,3,5,7,11,13,17]
    if len(digits)==10:
        for ii in range(1,8):
            d = 100*digits[ii]+10*digits[ii+1]+digits[ii+2]

            if d%prime_list[ii-1]==0:
                continue
            else:
                return False
    if len(digits)==9:
        for ii in range(0,7):
            d = 100*digits[ii]+10*digits[ii+1]+digits[ii+2]

            if d%prime_list[ii-1]==0:
                continue
            else:
                return False    

    return True

def build_pandigital_list(n):
    temp = list(itertools.permutations(range(n+1)))

    p_terms = []
    
    for ele in temp:
        term = ''
        for ii in ele:
            term+=str(ii)
        p_terms.append(int(term))
        
    return p_terms
    

def main():
    pan_sum = 0

    pan_list = build_pandigital_list(9)

    for p in pan_list:
        if check_substring_properties(p):
            pan_sum+=p
            print p

    return pan_sum

print main() 

    
