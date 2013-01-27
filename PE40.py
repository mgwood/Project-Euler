'''Project Euler #40

'''
import time

def build_champernowne(n):
    champ_str = ''

    ii = 1
    while len(champ_str)<n:
        champ_str+=str(ii)
        ii+=1

    return champ_str

def main():
    s = time.time()
    
    champ_str = build_champernowne(1000000)

    champ_product = 1

    champ_product*=int(champ_str[1-1])
    champ_product*=int(champ_str[10-1])
    champ_product*=int(champ_str[100-1])
    champ_product*=int(champ_str[1000-1])
    champ_product*=int(champ_str[10000-1])
    champ_product*=int(champ_str[100000-1])
    champ_product*=int(champ_str[1000000-1])

    return [champ_product,time.time()-s]
