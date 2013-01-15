tri_file = open("tri_2.txt","r")

Tri_array = []
for ii in range(15):
    Array = []
    Sub = []
    for ele in tri_file.readline():
        if ele==" " or ele=="\n":
            if len(Sub)==2:
                N = 10*int(Sub[0])+int(Sub[1])
            else:
                N = int(Sub[0])
            Array.append(N)
            #print N
            Sub = []
        else:
            Sub.append(ele)
    if len(Tri_array)==14:
        if len(Sub)==2:
            N = 10*int(Sub[0])+int(Sub[1])
        else:
            N = int(Sub[0])
        Array.append(N)

    Tri_array.append(Array)

print Tri_array
