function is_prime(n::Int)

        if n<= 0
                return false
        end

        if n==2 || n==3
                return true
        end

        if !((n%6==1) || (n%6==5))
                return false
        end

        root_list = [2,3]

        for k=1:ceil(sqrt(n)/6)
                a = 6*k-1
                b = 6*k+1
                if b<=sqrt(n)
                        append!(root_list,[a,b])
                        continue
                end
                if a<=sqrt(n)
                        append!(root_list,[a])
                        break
                end
        end

        for ii in root_list
            if n%ii == 0
                    return false
            end
        end

        return true

end

function prime_list(n::Int)
        p_list = [2,3]

        for ii = 5:n
                if is_prime(ii)
                        append!(p_list,[ii])
                end
        end
        return p_list
 end

function prime_list_length(n::Int)
        return length(prime_list(n))
end

function find_prime_factors(n)
        if n==1
                return [1 1]
                end
        if is_prime(n)
                return [n 1]
                end

        potential_primes = [2,3]
        ii = 1
        lim_1 = floor(n/2+1)
        while 6*ii<=lim_1
                append!(potential_primes,[6*ii-1])
                append!(potential_primes,[6*ii+1])
                ii+=1
        end

        limit = length(potential_primes)
        prime_factors = Int[]
        factor_count = Int[]
        for jj in potential_primes
                if n%jj == 0
                        if is_prime(jj)
                                append!(prime_factors,[jj])
                                append!(factor_count,[1])
                                new_div = n
                        end
                                while (new_div/jj)%jj==0
                                        factor_count[endof(factor_count)]+=1
                                        new_div = new_div/jj
                                end
                 end
                jj+=1
        end

        return [prime_factors factor_count]
end

function get_reduced_fraction(a,b)
        if a==b
                return [1,1]
                end
        if a==0
                return [0,1]
                end
        if b==0
                return "divide by zero error"
                end

        A_factors =  find_prime_factors(a)
        #println(A_factors)
        B_factors =  find_prime_factors(b)
        #println(B_factors)
        if length(A_factors[1])>length(B_factors[1])
                limiting_list = B_factors
                non_limiting = A_factors
        else
                limiting_list = A_factors
                non_limiting = B_factors
        end

        for ii=1:length(limiting_list[:,1])
                #println("in1")
                #println(ii)
                if in(limiting_list[ii,1],non_limiting[:,1])
                        #println("in2")
                        non_power=0
                        for jj=1:length(non_limiting[:,1])
                                #println("in3")
                                #println(jj)
                                #println(length(non_limiting))
                                #println(size(non_limiting))
                                #println(non_limiting[jj,1])
                                #println(limiting_list[ii,1])
                                if non_limiting[jj,1] == limiting_list[ii,1]
                                        #println("in4")
                                        non_power = non_limiting[jj,2]
                                        #println("non_power")
                                        #println(non_power)
                                        break
                                end
                        end
                        #remove duplicates
                        #println("here")
                        #println(limiting_list)
                        #println(size(limiting_list))
                        #println(limiting_list[ii,2])
                        #println(non_power)
                        if limiting_list[ii,2]>non_power
                                #println("in5")
                                com = limiting_list[ii,1]^(non_power)
                        else
                                #println("in6")
                                com = limiting_list[ii,1]^(limiting_list[ii,2])
                        end
                #println("common")
                #print(com)
                        a = a/com
                        b = b/com
                 end
        end
        return [int(a) int(b)]
end
