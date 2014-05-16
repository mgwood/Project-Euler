import math
import mwmath
import time

s = time.time()

def reduce_rows(row1,row2):
    new_row = []

    for ind in range(len(row1)):
        new_row.append(row1[ind]+min([row2[ind],row2[ind+1]]))

    return new_row

def compute_tri(tri):
    if len(tri)==2:
        return reduce_tri_rows(tri[0],tri[1])

    final_row = reduce_tri_rows(tri[len(tri)-2],tri[len(tri)-1])

    new_tri = []

    for ii in range(len(tri)-2):
        new_tri.append(tri[ii])

    new_tri.append(final_row)

    return compute_tri(new_tri)


test = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]

def get_rows(matrix,move_count):
    l = len(test)
    m = l-move_count-1 #lower left edge element
    
    row1 = []
    row2 = []

    for ii in range(l-m):
        print range(l-m)
        print matrix[l-1][ii]

    return [row1,row2]

get_rows(test,3)

'''
tri_file = open("triangle.txt","r")


Tri_array = []
for ii in range(100):
    Array = []
    Sub = []
    for ele in tri_file.readline():
        if ele==" " or ele=="\n":
            if len(Sub)==2:
                N = 10*int(Sub[0])+int(Sub[1])
            else:
                N = int(Sub[0])
            Array.append(N)
            #print N
            Sub = []
        else:
            Sub.append(ele)
    #if len(Tri_array)==98:
    #    if len(Sub)==2:
    #        N = 10*int(Sub[0])+int(Sub[1])
    #    else:
    #        N = int(Sub[0])
    #    Array.append(N)

    Tri_array.append(Array)

print Tri_array
print compute_tri(Tri_array)

tri_file.close()

print time.time()-s
'''
