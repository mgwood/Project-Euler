'''Project Euler #17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23
letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

'''
import time

def number_letter_count(n,letter_dict):
    thousands = int(n/1000)
    hundreds = int((n%1000)/100)
    tens = int((n%100)/10)
    ones = int((n%10))
    teens = int((n%100))

    letter_count = 0

    if thousands>0:
        letter_count+=letter_dict[thousands]
        letter_count+=letter_dict[1000]
    if hundreds>0:
        letter_count+=letter_dict[hundreds]
        letter_count+=letter_dict[100]
    if hundreds>0 and not (tens==0 and ones==0):
        letter_count+=3 #and

    if tens>1 or tens==0: #all but teens
        letter_count+=letter_dict[tens*10]
        letter_count+=letter_dict[ones]

    elif tens==1 and ones==0:
        letter_count+=letter_dict[10]
    else:#teens
        letter_count+=letter_dict[teens]
        
    return letter_count

def main():
    s = time.time()

    letter_dict={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,
             15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,
             80:6,90:6,100:7,1000:8}

    total_count = 0

    for ii in range(1,1001):
        total_count+=number_letter_count(ii,letter_dict)

    return [total_count,time.time()-s]
