'''Project Euler #34

'''
import itertools
import mwmath

def is_permute(a,b):
        if not len(str(a))==len(str(b)):
            return False
        
        b_dig = mwmath.get_digits(b)
        for dig in mwmath.get_digits(a):
                if dig in b_dig:
                        b_dig.remove(dig)
                else:
                        return False

        return True

def main():
    ii = 1
    while True:
        if is_permute(ii,ii*6):
            if is_permute(ii,ii*5):
                if is_permute(ii,ii*4):
                    if is_permute(ii,ii*3):
                        if is_permute(ii,ii*2):
                            return ii
        ii+=1









                    
