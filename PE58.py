'''Project Euler #58

'''
import mwmath

def get_spiral_terms(n,spiral):
    
    spiral.append(n**2)
    spiral.append(n**2-(n-1))
    spiral.append(n**2-2*(n-1))
    spiral.append(n**2-3*(n-1))

    return spiral
    
def find_prime_ratio(spiral,previous_p):
    prime_elements = 0
    for ii in spiral[len(spiral)-4:]:
        if mwmath.is_prime(ii):
            prime_elements+=1

    return [prime_elements+previous_p,1.0*(prime_elements+previous_p)/len(spiral)]

def main():

    spiral = [1]

    limit = 30000
    
    t = [2*x+1 for x in range(1,limit+1)]
    ratio = 1
    previous_p = 0
    for ii in t:
        spiral = get_spiral_terms(ii,spiral)
        [previous_p,ratio] = find_prime_ratio(spiral,previous_p)
        
        if ratio<0.1:
            return ii
        
    return "Not found: "+str(ratio)

print main()
