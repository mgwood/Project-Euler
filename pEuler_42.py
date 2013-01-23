import math
import mwmath
import time

s = time.time()

def score_word(word):
    letter_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,
                   'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,
                   'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26,
                   '"':0,' ':0,',':0,"'":0,'[':0,']':0}

    word_score = 0
    
    for letter in word:
        word_score+=letter_dict[letter]

    return word_score

def build_word_list(data):
    word_list = []
    word = ''

    for ele in data:
        if ele!=',':
            word+=ele
        else:
            word_list.append(word)
            word = ''
    word_list.append(word)

    return word_list
            
#find triangle numbers up to 15*26
tri_list = []
tri_n = 1
ii = 1
while tri_n<15*26:
    tri_n = mwmath.get_triangle_n(ii)
    tri_list.append(tri_n)

    ii+=1

word_file = open("words.txt","r")
data = word_file.readlines()
word_file.close()

word_list = build_word_list(str(data))

word_count = 0

for ele in word_list:
    if ele != '"':
        word_score = score_word(ele)

        if word_score in tri_list:
            word_count+=1

print word_count


print time.time()-s
