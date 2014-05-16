function main()
tic()
        data = readcsv("/Users/michaelwood/Documents/Julia/base_exp.txt")
        curmax = 0
        curmax_row = 0

        for ii=1:1000
              temp = data[ii,2]*log(data[ii,1])
              if temp>curmax
                      curmax=temp
                      curmax_row=ii
              end
        end

println(curmax_row)
toq()
end
