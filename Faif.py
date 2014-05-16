'''
Faif analysis
'''

skulls = range(1,5)
bonus = 3

max_val = 0
max_skull = 0


for ii in skulls:
    swords = range(1,5-ii+1)

    print str(ii)+' skull'
    for jj in swords:
        expected_val = 0.2*jj*(ii+bonus)-0.2*ii
        print str(jj)+' swords: '+str(expected_val)
    
