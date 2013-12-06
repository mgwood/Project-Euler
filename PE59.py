'''Project Euler #58

'''
import mwmath


lines = (line.rstrip('\n') for line in open("cipher1.txt"))
text = lines.next()

encrypted_text_a = []
encrypted_text_b = []
encrypted_text_c = []
count = 0
buff = ''

for ii in text:
    if ii==',':
        if count%3==0:
            encrypted_text_a.append(buff)
        if count%3==1:
            encrypted_text_b.append(buff)
        if count%3==2:
            encrypted_text_c.append(buff)
        count +=1
        buff = ''
    else:
        buff = buff+ii
else:
    if count%3==0:
        encrypted_text_a.append(buff)
    if count%3==1:
        encrypted_text_b.append(buff)
    if count%3==2:
        encrypted_text_c.append(buff)

#print encrypted_text_a
#print len(encrypted_text_a)

#print ord('A')
#print ord('Z')
cipher_lower_limit = ord('a')
cipher_upper_limit = ord('z')

cipher_Lower_Limit = ord('A')
cipher_Upper_Limit = ord('Z')

a_trials = []
b_trials = []
c_trials = []

for jj in range(ord('a'),ord('z')+1):
    letter_switch = True
    through = 0
    for kk in encrypted_text_a:
        #print kk
        t = int(kk)^jj
        if (t>=cipher_lower_limit) and (t<=cipher_upper_limit):
            pass
        else:
            if (t>=cipher_Lower_Limit) and (t<=cipher_Upper_Limit):
                pass
            else:
                if t in [32,33,34,39,40,41,44,46,48,49,50,51,52,53,54,55,56,57,58,59,63,96,38,45,123,125,47,36,35]:
                    pass
                else:
                    #print chr(jj)
                    #print chr(t)
                    letter_switch = False
                    break
        through += 1
        
    if letter_switch:
        a_trials.append(jj)

for jj in range(ord('a'),ord('z')+1):
    letter_switch = True
    through = 0
    for kk in encrypted_text_b:
        #print kk
        t = int(kk)^jj
        if (t>=cipher_lower_limit) and (t<=cipher_upper_limit):
            pass
        else:
            if (t>=cipher_Lower_Limit) and (t<=cipher_Upper_Limit):
                pass
            else:
                if t in [32,33,34,39,40,41,44,46,48,49,50,51,52,53,54,55,56,57,58,59,63,96,38,45,123,125,47,36,35]:
                    pass
                else:
                    #print chr(jj)
                    #print chr(t)
                    letter_switch = False
                    break
        through += 1
        
    if letter_switch:
        b_trials.append(jj)

for jj in range(ord('a'),ord('z')+1):
    letter_switch = True
    through = 0
    for kk in encrypted_text_c:
        #print kk
        t = int(kk)^jj
        if (t>=cipher_lower_limit) and (t<=cipher_upper_limit):
            pass
        else:
            if (t>=cipher_Lower_Limit) and (t<=cipher_Upper_Limit):
                pass
            else:
                if t in [32,33,34,39,40,41,44,46,48,49,50,51,52,53,54,55,56,57,58,59,63,96,38,45,123,125,47,36,35]:
                    pass
                else:
                    #print chr(jj)
                    #print chr(t)
                    letter_switch = False
                    break
        through += 1
        
    if letter_switch:
        c_trials.append(jj)

def decrypt_text():

    return True

