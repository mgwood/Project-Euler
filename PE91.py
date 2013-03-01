'''Project Euler #91

'''
import mwmath


def is_right_tri(pts):
    x = pts[0::2]
    y = pts[1::2]

    combos = [0,1,0,2,1,2]

    for ii in range(0,3):
        x1 = x[combos[2*ii]]
        x2 = x[combos[2*ii+1]]
        y1 = y[combos[2*ii]]
        y2 = y[combos[2*ii+1]]
        
        if (x1==x2) and (y1==y2):
            return False
    
    x_diff = [(x[0]-x[1]),(x[0]-x[2]),(x[1]-x[2])]
    y_diff = [(y[0]-y[1]),(y[0]-y[2]),(y[1]-y[2])]

    dot_products = []
    
    for ii in range(0,3):
        x1 = x_diff[combos[2*ii]]
        x2 = x_diff[combos[2*ii+1]]
        y1 = y_diff[combos[2*ii]]
        y2 = y_diff[combos[2*ii+1]]
        
        dot_product = (x1*x2)+(y1*y2)
        if dot_product == 0:
            return True
    
    return False

#print is_right_tri([0,2,1,1,0,0])
#print is_right_tri([1,2,1,1,0,0])
#print is_right_tri([1,1,1,1,0,0])
#print is_right_tri([0,1,1,0,0,0])

r_tri_count = 0

upper_limit = 50

for x1 in range(0,upper_limit+1):
    for y1 in range(0,upper_limit+1):
        for x2 in range(0,upper_limit+1):
            for y2 in range(0,upper_limit+1):
                if is_right_tri([x1,y1,x2,y2,0,0]):
                    r_tri_count+=1

print r_tri_count/2

def main():

    return 1

    
