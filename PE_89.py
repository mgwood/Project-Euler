'''Project Euler #89
'''
import mwmath

def write_roman(n,s):
    romans = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}

    test_vals = romans.keys()
    test_vals.sort()
    test_vals.reverse()

    for t in test_vals:
        if n-t==0:
            s+=romans[t]
            return s
        if n-t>0:
            s+=romans[t]
            return write_roman(n-t,s)

def parse_roman(s):
    romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    s = s[::-1]

    cur_sum = romans[s[0]]

    for ii in range(1,len(s)):
        if romans[s[ii]]>=romans[s[ii-1]]:
            cur_sum+= romans[s[ii]]
        else:
            cur_sum-= romans[s[ii]]

    return cur_sum

def build_roman_list(f_name):
    r_list = []
    for r in open(f_name).read().strip().split('\n'):
        r_list.append(r)

    return r_list

def main():
    r_list = build_roman_list('roman.txt')

    saved = 0
    
    for r in r_list:
        digits =  len(r)
        min_digits= len(write_roman(parse_roman(r),''))

        saved += (digits-min_digits)

    return saved

print main()
