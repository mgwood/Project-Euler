import math
import mwmath
import time

s = time.time()

letter_dict={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,
             15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,
             80:6,90:6,100:7,1000:8}

def number_letter_count(n,letter_dict):
    thousands = int(n/1000)
    hundreds = int((n%1000)/100)
    tens = int((n%100)/10)
    ones = int((n%10))
    teens = int((n%100))

    #print "thousands: "+str(thousands)
    #print "hundreds: "+str(hundreds)
    #print "tens: "+str(tens)
    #print "ones: "+str(ones)

    letter_count = 0

    if thousands>0:
        letter_count+=letter_dict[thousands]
        letter_count+=letter_dict[1000]
        #print "Adding Th: "+str(letter_dict[thousands])
        #print "Adding Th: "+str(letter_dict[1000])
    if hundreds>0:
        letter_count+=letter_dict[hundreds]
        letter_count+=letter_dict[100]
        #print "Adding Hu: "+str(letter_dict[hundreds])
        #print "Adding Hu: "+str(letter_dict[100])
    if hundreds>0 and not (tens==0 and ones==0):
        letter_count+=3 #and
        #print "Adding 3: "+str(3)

    if tens>1 or tens==0: #all but teens
        letter_count+=letter_dict[tens*10]
        letter_count+=letter_dict[ones]

        #print "Adding Tens: "+str(letter_dict[tens*10])
        #print "Adding Ones: "+str(letter_dict[ones])
    elif tens==1 and ones==0:
        letter_count+=letter_dict[10]
    else:#teens
        letter_count+=letter_dict[teens]
        
    return letter_count



total_count = 0

for ii in range(1,1001):
    print str(ii)+" "+str(number_letter_count(ii,letter_dict))
    total_count+=number_letter_count(ii,letter_dict)

print total_count

print time.time()-s
