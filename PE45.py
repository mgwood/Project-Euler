'''Project Euler #45

'''

import mwmath
import time

def build_tri_list(n):
    tri_list = [1]
    for ii in range(1,n+1):
        tri_list.append(tri_list[-1]+ii+1)

    return tri_list


def build_pent_list(n):
    pent_list = [1]
    for ii in range(1,n+1):
        pent_list.append(pent_list[-1]+3*ii+1)

    return pent_list

def build_hex_list(n):
    hex_list = [1]
    for ii in range(1,n+1):
        hex_list.append(hex_list[-1]+4*ii+1)

    return hex_list

def find_coincident_t_p_h(hit_limit):
    hits = 0
    hit_list = []
    
    tri_list = build_tri_list(80000)
    pent_list = build_pent_list(40000)
    hex_list = build_hex_list(30000)
    
    while hits<hit_limit:
        for h in hex_list:
            if (h in pent_list) and (h in tri_list):
                print h
                hit_list.append(h)
                hits+=1

                if hits>=hit_limit:
                    return hit_list
                else:
                    hex_list.remove(h)
                    break
            else:
                hex_list.remove(h)

        if len(hex_list)==0:
            print "Not enough hits found -- raise limit"
            return hit_list

    return hit_list

def main():
    s = time.time()

    return [find_coincident_t_p_h(3),time.time()-s]
