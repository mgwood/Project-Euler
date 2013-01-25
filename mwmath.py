import math

def perfect_square(n):
	if math.floor(math.sqrt(n))==n/math.sqrt(n):
		return True
	return False

def fibb(n):
    n = math.floor(n)
    if n<=1:
        return 1
    elif n==2:
        return 1
    else:
        return fibb(n-2)+fibb(n-1)

def is_pal(n):
	n = str(n)
	palendrome = True

	ii = 0
	while ii<math.floor(len(n)/2):
		if n[ii]!=n[len(n)-1-ii]:
			palendrome = False
		
		ii = ii+1

	return palendrome

def pascal_row(n):
        if n == 0:
                return [1.0]
        row = [1.0]
        r = n+1
        for ii in range(n):
                c = ii+1.0
                next_term = row[ii]*((r-c)/c)
                row.append(next_term)

        return row

def is_prime(n):
        prime = True
        if n<=1:
                return False
        if n==2 or n==3:
                return prime
        
        potential_primes = [2,3]
        ii = 1
        while 6*ii<=(math.sqrt(n)+6):
                potential_primes.append(6*ii-1)
                potential_primes.append(6*ii+1)
                ii+=1

        jj = 0
        limit = len(potential_primes)
        while jj<limit:
                if n%potential_primes[jj] == 0 and potential_primes[jj]<n:
                        prime = False
                jj+=1
        
        return prime

def find_prime_factors(n):
        if n==1:
                return [[1],[1]]
        if is_prime(n):
                return [[n],[1]]
        
        potential_primes = [2,3]
        ii = 1
        lim_1 = math.floor(n/2+1)
        while 6*ii<=lim_1:
                potential_primes.append(6*ii-1)
                potential_primes.append(6*ii+1)
                ii+=1

        
        limit = len(potential_primes)
        prime_factors = [];
        factor_count = [];
        for jj in potential_primes:
                if n%jj == 0:
                        if is_prime(jj):
                                prime_factors.append(jj)
                                factor_count.append(1)
                                new_div = n
                                while (new_div/jj)%jj==0:
                                        factor_count[-1]+=1
                                        new_div = new_div/jj
                jj+=1
        
        return [prime_factors,factor_count]

def find_factors(n):
        n = math.floor(n)

        factors = [1]

        ii = 2
        while ii<=((n+2)/2):
                if n%ii==0:
                        factors.append(ii)
                ii+=1
        return factors

def find_factors2(n):
        p_facts = find_prime_factors(n)

        factors = p_facts[0]
        factors.append(1)
        powers = p_facts[1]

        for kk in range(max(powers)):
                for ii in factors:
                        for jj in factors:
                                f_prime = ii*jj
                                if f_prime<n and (n%f_prime==0):
                                        if not (f_prime in factors):
                                                factors.append(f_prime)
                                else:
                                        break
        return factors

def sumOfFactors(n):

    factors = find_factors2(n)

    return sum(factors)

def is_perfect(n):
        sum_factors = sumOfFactors(n)

        if sum_factors==n:
                return True
        return False

def is_abundant(n):
        sum_factors = sumOfFactors(n)

        if sum_factors>n:
                return True
        return False

def count_factors(n):
        n = math.floor(n)
        prime_factorization = find_prime_factors(n)

        factor_count = 1

        ii = 0
        limit = len(prime_factorization[1])

        while ii<limit:
                factor_count*=(prime_factorization[1][ii]+1)
                ii+=1

        return factor_count

def r_factorial(n):
    
    if n<=1:
        return 1
    else:
        return n*r_factorial(n-1)

def rotate_digits(n):
    str_n = str(n)
    rotated_n = [str_n[1]]
    for ii in str_n[2:(len(str_n))]:
        rotated_n.append(ii)

    rotated_n.append(str_n[0])

    power = len(rotated_n)-1
    rotated = 0
    for jj in rotated_n:
        rotated+=int(jj)*10**power

        power-=1
    
    return rotated

def get_triangle_n(n):
        if n<=1:
                return 1
        else:
                return n+get_triangle_n(n-1)

def circ_digit_check(n):
        str_n=str(n)
        if '2' in str_n:
                return False
        if '4' in str_n:
                return False
        if '6' in str_n:
                return False
        if '8' in str_n:
                return False
        if '5' in str_n:
                return False
        if '0' in str_n:
                return False

        return True

def nr_factorial(n):
    n = math.floor(n)

    product = 1
    if n<=1:
        return product
    else:
        ii=2
        while ii<=n:
            product*=ii
            ii+=1

        return product

def count_digits(n):
    return len(str(n))

def count_digits2(n):
        return 1+math.floor(math.log10(n))


def get_digits(n):
    return map(int,str(n))

def is_pandigital(n):
        pan_len = count_digits(n)
        pan_array = range(1,pan_len+1)
        is_pan = True


        for dig in get_digits(n):
                if dig in pan_array:
                        pan_array.remove(dig)
                else:
                        is_pan=False

        return is_pan
