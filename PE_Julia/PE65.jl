function build_e_list(n::Int)
    if n<=3
        if n==1
                return [2]
                end
        if n==2
                return [2,1]
                end
        if n==3
                return [2,1,2]
                end
    end

    e_list = [2,1,2]

    for ii = 1:(floor((n-1)/3)-1)
            append!(e_list,[1,1,2*(ii+1)])
    end

    if n%3==0
        append!(e_list,[1,1,2*(n/3)])
    end
    if n%3==1
        append!(e_list,[1])
    end
    if n%3==2
        append!(e_list,[1,1])
    end

return e_list
end

function continued_fraction(A)
        #println(A)
        #println("next num")
        #println(A[3]*A[2]+A[1])
    return [BigInt(A[3]*A[1]+A[2]), BigInt(A[1])]
    #A = [Numerator, Denomenator, next element]
end

function digit_sum(n::Int,runsum::Int)
    if n<10
            return n+runsum
    end
    return digit_sum((floor(n/10)),runsum+n%10)
end

function main(n::Int)
tic()
    e_list = build_e_list(n)
    #println(e_list)
    A = [pop!(e_list),1,pop!(e_list)]
    #println(A)
    B = [1,1]
    for ii=1:(n-1)
        B = continued_fraction(A)
        #println('B')
        #println(B)
        if length(e_list)>=1
                A = [B[1],B[2],[pop!(e_list)]]
        end
    end
    println(B[1])
    println(B[2])
    #println(digit_sum(B[1],0))
toc()
end

