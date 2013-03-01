'''Project Euler #31
'''

coins = [1,2,5,10,20,50,100,200]
limit = 50
max_c = []

for ii in range(len(coins)):
    max_c.append(limit/coins[ii]+1)

#print max_c

def check_change(count,coins,limit):
    s = 0
    for ii in range(len(coins)):
        s += count[ii]*coins[ii]

    return s

#print check_change([3,1,1,0,2,1,1,0],coins,limit)

if limit==200:
    ways = 1
else:
    ways = 0

for a in range(max_c[6]):
    run_sum = a*coins[6]
    if run_sum==limit:
        ways+1
        break
    for b in range(max_c[5]):
        run_sum += b*coins[5]
        if run_sum>limit:
            run_sum = 0
            break
        if run_sum==limit:
            ways+=1
            run_sum = a*100
            break
        for c in range(max_c[4]):
            run_sum += c*coins[4]
            if run_sum>limit:
                run_sum = 0
                break
            if run_sum==limit:
                ways+=1
                run_sum = a*100+b*50
                break
            for d in range(max_c[3]):
                run_sum += d*coins[3]
                if run_sum>limit:
                    run_sum = 0
                    break
                if run_sum==limit:
                    ways+=1
                    run_sum = a*100+b*50+c*20
                    break
                for e in range(max_c[2]):
                    run_sum += e*coins[2]
                    if run_sum>limit:
                        run_sum = 0
                        break
                    if run_sum==limit:
                        ways+=1
                        run_sum = a*100+b*50+c*20+d*10
                        break
                    for f in range(max_c[1]):
                        run_sum += f*coins[1]
                        if run_sum>limit:
                            run_sum = 0
                            break
                        ways+=1
                        #print "100: "+str(a)
                        #print "50: "+str(b)
                        #print "20: "+str(c)
                        #print "10: "+str(d)
                        #print "5: "+str(e)
                        #print "2: "+str(f)
                        #print run_sum
                        run_sum = a*100+b*50+c*20+d*10+e*5
                        if run_sum>limit:
                            ways-=1
                            break
                        
                        
                                

print "done"
print ways
def main():
    1
