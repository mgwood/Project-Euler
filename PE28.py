'''Project Euler #28

'''

import time

def spiral_sum(n):
    if n<=1:
        return 1
    else:
        add = (n**2)+ (n**2 - (n-1))+ (n**2 - 2*(n-1))+ (n**2 - 3*(n-1))
        return add+spiral_sum(n-2)


def main():
    s = time.time()

    return [spiral_sum(1001),time.time()-s]
