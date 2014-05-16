'''Project Euler #68
For magic 3-gon

a+b+c = n
d+c+e = n
f+e+b = n

a<d and a<f
a,b,c,d,e,f are in 1-6


for magic 5-gon

a+b+c = n
d+c+e = n
f+e+g = n
h+g+i = n
j+i+b = n

a-j in 1-10, no repeating
one of d,f,h,j = 10

a<d, a<f, a<h, a<j

1. find largest a (6 at most) that works
2. find all a=largest that work and pick largest b

'''
import mwmath_2
import time
import itertools


def check_n_gon(gon,n):
    if n == 3:

        a = gon[0]
        b = gon[1]
        c = gon[2]
        d = gon[3]
        if not gon[4]==c:
            print 'bad gon'
            return False
        e = gon[5]
        f = gon[6]
        if not gon[7]==e:
            print 'bad gon'
            return False
        if not gon[8]==b:
            print 'bad gon'
            return False
        
        check = a+b+c

        if not d+c+e==check:
            return False
        if not f+e+b==check:
            return False


    if n == 5:
        a = gon[0]
        b = gon[1]
        c = gon[2]
        d = gon[3]
        if not gon[4]==c:
            print 'bad gon'
            return False
        e = gon[5]
        f = gon[6]
        if not gon[7]==e:
            print 'bad gon'
            return False
        g = gon[8]
        h = gon[9]
        if not gon[10]==g:
            print 'bad gon'
            return False
        i = gon[11]
        j = gon[12]
        if not gon[13]==i:
            print 'bad gon'
            return False
        if not gon[14]==b:
            print 'bad gon'
            return False
        
        check = a+b+c

        if not d+c+e==check:
            return False
        if not f+e+g==check:
            return False
        if not h+g+i==check:
            return False
        if not j+i+b==check:
            return False
        

    return True

def check_n_gon_2(a,b,c,d,e,f,g,h,i,j):
    check = a+b+c

    if not d+c+e==check:
        return False
    if not f+e+g==check:
        return False
    if not h+g+i==check:
        return False
    if not j+i+b==check:
        return False
        

    return True
    

#print check_n_gon([1,6,5,3,5,4,2,4,6],3)
        
gon_list = 1,2,3,4,5,7,8,9,10
a = 6
gon_gen = itertools.permutations(gon_list,9)
#b = 0, c = 1, d = 2, e = 3, f = 4, g = 5, h = 6, i = 7, j = 8
for ii in gon_gen:
    if not (ii[2]==10) or (ii[4]==10) or (ii[6]==10) or (ii[8]==10):
        continue
    else:
        if check_n_gon_2(6,ii[0],ii[1],ii[2],ii[3],ii[4],ii[5],ii[6],ii[7],ii[8]):
            print a,ii

#one of d,f,h,j = 10
