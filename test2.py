print len([])

for a in range(10):

    print 'a'
    print a
    for b in range(3):
        print 'b1'
        print b
        if b<2:
            continue
        print 'b2'
        print b
