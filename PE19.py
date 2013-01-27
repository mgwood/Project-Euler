'''Project Euler #19
'''
import time

def num_yearly_sundays(year,jan_1_day):
    month_lengths = {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
    if is_leap_year(year):
        month_lengths[1] = 29

    #Mon=0,Tues=1,Wed=2,Thurs=3,Fri=4,Sat=5,Sun=6 check if first_day%7==6
    first_days = [jan_1_day]
    for ii in range(1,12):
        first_days.append(first_days[ii-1]+month_lengths[ii-1])

    sun_count = 0
    for jj in first_days:
        if jj%7==6:
            sun_count+=1

    return sun_count

def is_leap_year(n):
    if not n%4==0:
        return False
    if n%100==0:
        if n%400==0:
            return True
        return False
    return True


def main():
    s = time.time()
    
    sun_total = 0
    jan_1_1900 = 0
    jan_1_day = (jan_1_1900+365)%7
    for ii in range(1901,2001):
        #print jan_1_day
        sun_total+=num_yearly_sundays(ii,jan_1_day)

        if not is_leap_year(ii):
            jan_1_day = (jan_1_day+365)%7
        else:
            jan_1_day = (jan_1_day+366)%7  
  
    return [sun_total,time.time()-s]
