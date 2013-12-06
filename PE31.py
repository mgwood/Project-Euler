'''Project Euler #31
'''
def coin_sum(coin_count,coins):
    val = 0
    for ii in range(len(coin_count)):
        val = val+coin_count[ii]*coins[ii]
    return val

def reset_coins():
    coin_count = [0,0,0,0,0,0,0,0]
    return coin_count

def reset_lower_coins(coin_count,n):
    for ii in range(n+1,len(coin_count)):
        coin_count[ii]=0
    return coin_count       

coins = [200,100,50,20,10,5,2,1]
coin_count = [0,0,0,0,0,0,0,0]
max_c = [2,3,5,11,21,41,101,201]
check = 200
w=0

for a in range(max_c[0]):
    #add 200p
    reset_coins()
    coin_count[0] = a
    r = coin_sum(coin_count,coins)
    if r>check:
        continue
    if r==check:
        w = w+1
        continue
    
    for b in range(max_c[1]):
        #add 100p
        reset_lower_coins(coin_count,1)
        coin_count[1] = b
        r = coin_sum(coin_count,coins)
        if r>check:
            continue
        if r==check:
            w = w+1
            continue
        
        for c in range(max_c[2]):
            #add 50p
            reset_lower_coins(coin_count,2)
            coin_count[2] = c
            r = coin_sum(coin_count,coins)
            if r>check:
                continue
            if r==check:
                w = w+1
                continue

            for d in range(max_c[3]):
                #add 20 p
                reset_lower_coins(coin_count,3)
                coin_count[3] = d
                r = coin_sum(coin_count,coins)
                if r>check:
                    continue
                if r==check:
                    w = w+1
                    continue
                
                for e in range(max_c[4]):
                    #add 10p
                    reset_lower_coins(coin_count,4)
                    coin_count[4] = e
                    r = coin_sum(coin_count,coins)
                    if r>check:
                        continue
                    if r==check:
                        w = w+1
                        continue
                    
                    for f in range(max_c[5]):
                        #add 5p
                        reset_lower_coins(coin_count,5)
                        coin_count[5] = f
                        r = coin_sum(coin_count,coins)
                        if r>check:
                            continue
                        if r==check:
                            w = w+1
                            continue
                        
                        for g in range(max_c[6]):
                            #add 2p
                            reset_lower_coins(coin_count,6)
                            coin_count[6] = g
                            r = coin_sum(coin_count,coins)
                            if r>check:
                                continue
                            if r==check:
                                w = w+1
                                continue

                            for h in range(max_c[7]):
                                #add 1p
                                coin_count[7] = h
                                r = coin_sum(coin_count,coins)
                                if r>check:
                                    continue
                                if r<=check:
                                    w = w+1
                                    continue
                    
print "done"
print w+1
