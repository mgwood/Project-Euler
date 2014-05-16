include("/Users/michaelwood/Documents/Julia/mwmath.jl")

function check_fraction(A, L)

        t = indexin(A,L)
        println(t)
        println(L)
        if (t[2]-t[1])==length(L)/2
                return true
        else
                return false
        end

end

function get_int_length(n::Int)
        return ifloor(log10(n))+1
end

function compact_fraction(A)
   return A[1]*10^(get_int_length(A[2]))+A[2]
end

function build_fraction_list(d)
tic()
        L = [1 d]
        L_1d = Int[]

        #d loop
        for ii = 2:d
                #n loop
                flag = true
                for jj = 1:(iceil(ii/2))
                   if flag
                        if (jj/ii)<(1/3)
                                continue
                        end
                        if (jj/ii)>(1/2)
                               flag = false
                                continue
                        end
                        A = get_reduced_fraction(jj,ii)
                        if A != [jj ii]
                                continue
                        end
                        A_1d = compact_fraction(A)
                        #println(A)
                        #println(L)
                        #println(check_fraction(A,L))
                        if in(A_1d,L_1d)
                                continue
                        else
                                append!(L_1d,[A_1d])
                        end
                  end
                end
        end
toc()
        return L_1d
end
