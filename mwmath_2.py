import math

def perfect_square(n):
        if n<1:
                return False
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

def build_prime_list(n):
        potential_primes=[2,3]
        ii = 1
        while 6*ii<=(n):
                potential_primes.append(6*ii-1)
                potential_primes.append(6*ii+1)
                ii+=1

        prime_list=[]
        for jj in potential_primes:
                if is_prime(jj):
                        prime_list.append(jj)

        return prime_list

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
        n = int(n)

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

def is_permutation(a,b):
        if not len(str(a))==len(str(b)):
                return False
        dig_b = get_digits(b)
        
        for dig in get_digits(a):
                if dig in dig_b:
                        dig_b.remove(dig)
                else:
                        return False

        return True

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

    return hex_lis

def build_n_digit_prime_list(n):
        if n==1:
                potential_primes=[2,3]
        else:
                potential_primes=[]
        ii = int(1+(10**(n-1))/6)
        while 6*ii<=(10**n):
                potential_primes.append(6*ii-1)
                potential_primes.append(6*ii+1)
                ii+=1

        prime_list=[]
        for jj in potential_primes:
                if is_prime(jj):
                        prime_list.append(jj)

        return prime_list

def build_prime_permutations_list(n):

    import itertools
    p_list = list(itertools.permutations(get_digits(n)))
    
    p_terms = []
    digit_count = len(str(n))
    
    for ele in p_list:
        term = ''
        for ii in ele:
            term+=str(ii)
        p_terms.append(int(term))
        
    prime_p_terms = []
    
    for ii in p_terms:
        if ii in prime_p_terms:
                continue
        if len(str(ii))!=digit_count:
                continue
        if ii%2==0:
            continue
        if ii%3==0:
            continue
        if ii%5==0:
            continue
        if is_prime(ii):
            prime_p_terms.append(ii)
    
    return prime_p_terms


def most_frequent_digit_list(array):

        array = map(str,array)

        digit_count = range(len(array[0]))

        max_digit_list = []
        
        for jj in digit_count:
                
                cur_digit_list = []
                for ii in range(len(array)):
                        cur_digit_list.append(array[ii][0])
                        array[ii]=array[ii][1:]

                max_digit_list.append(most_frequent_ele(cur_digit_list))

        return max_digit_list
        

def most_frequent_ele(array):
        count_dict = {}
        
        for ele in array:
                if ele not in count_dict.keys():
                        count_dict[ele]=1
                else:
                        count_dict[ele]+=1

        max_val = -1
        freq = 0
        for key in count_dict.keys():
                if count_dict[key]>freq:
                        max_val = key
                        freq = count_dict[key]

        return [max_val,freq]

def concat_prime_list(n,m_list,p_list):
        result = True
        
        for m in m_list:
                result = result and concat_prime(n,m,p_list)

                if not result:
                        return False

        return True
                

def concat_prime(n,m,p_list):

        if min([int(str(n)+str(m)),int(str(m)+str(n))])>p_list[-1]:
                if is_prime(int(str(n)+str(m))):
                        return is_prime(int(str(m)+str(n)))
                else:
                        return False

        if int(str(n)+str(m)) not in p_list:
                return False
        if int(str(m)+str(n)) not in p_list:
                return False

        return True

def get_reduced_fraction(a,b):
        if a==b:
                return [1,1]
        if a==0:
                return [0,1]
        if b==0:
                return 'divide by zero error'

        
        A_factors =  find_prime_factors(a)
        
        B_factors =  find_prime_factors(b)

        if len(A_factors[0])>len(B_factors[0]):
                limiting_list = B_factors
                non_limiting = A_factors
        else:
                limiting_list = A_factors
                non_limiting = B_factors

        #print limiting_list
        #print non_limiting
        for ii in range(len(limiting_list[0])):
                if limiting_list[0][ii] in non_limiting[0]:

                        for jj in range(len(non_limiting[0])):
                                if non_limiting[0][jj] == limiting_list[0][ii]:
                                        non_power = non_limiting[1][jj]
                        
                        #print limiting_list[0][ii]
                        #remove duplicates
                        if limiting_list[1][ii]>non_power:
                                com = pow(limiting_list[0][ii],non_power)
                        else:
                                com = pow(limiting_list[0][ii],limiting_list[1][ii])
                #print com
                        a = a/com
                        b = b/com

        return [a,b]
                                
def build_sqrt2_continued_fraction_terms(n):
        cf_terms = [[1,2]];

        for ii in range(1,n+1):
                cf_terms.append(get_next_sqrt2_cf_term(cf_terms[ii-1][0],cf_terms[ii-1][1]))

        return cf_terms

def get_next_sqrt2_cf_term(prev_n,prev_d):
        return [prev_d, 2*prev_d+prev_n]

def get_actual_sqrt2_cf(n,d):
        #return get_reduced_fraction(n+d,d)
        return [n+d,d]
