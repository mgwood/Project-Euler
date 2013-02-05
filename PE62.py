''' Project Euler #62
'''

import itertools
import mwmath

def build_cube_list(lower_val,n):
    cube_list = []

    for ii in range(n):
        cube_list.append((lower_val+ii)**3)

    return cube_list

def build_perm_list(cube):
    perm_list = list(map("".join, itertools.permutations(str(cube))))
    perm_list = map(int,perm_list)
    perm_list.sort()

    c_length = len(str(cube))
    while True:
        if perm_list[0]<cube:
            perm_list.pop(0)
        else:
            break
    
    return perm_list

limit = 10**(-9)

lower_val = 344
#3 permutations occurs first at n=345
#4 permutations occurs first at n=1002
cube_list_length = 10000

cube_list = build_cube_list(lower_val,cube_list_length)

while True:
    if len(cube_list)==0:
        break
    perm_cubes = [cube_list[0]]
    
    for cube2 in cube_list[1:]:
        if mwmath.is_permutation(perm_cubes[0],cube2):
            if not cube2 in perm_cubes:
                perm_cubes.append(cube2)

    if len(perm_cubes)==5:
        print perm_cubes
        break
        

    cube_list.pop(0)

    
