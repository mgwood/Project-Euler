def build_prime_permutations_list(n):

    import itertools
    p_list = list(itertools.permutations(get_digits(n)))
    
    p_terms = []
    
    for ele in p_list:
        term = ''
        for ii in ele:
            term+=str(ii)
        p_terms.append(int(term))
        
    prime_p_terms = []
    
    for ii in p_terms:
        if ii%2==0:
            continue
        if ii%3==0:
            continue
        if ii%5==0:
            continue
        if is_prime(ii):
            prime_p_terms.append(ii)
    
    return prime_p_terms
