import time

s = time.time()

def compute_name_score(name):
    letter_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,
                   'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,
                   'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,
                   'Y':25,'Z':26,'"':0}

    word_score = 0

    for letter in name:
        word_score+=letter_dict[letter]

    return word_score

def build_name_list(f_name):
    names = []
    for name in open(f_name).read().strip().split(','):
        names.append(name)

    names.sort()
    return names

def calc_list_score(names):
    list_score = 0
    for ind in range(0,len(names)):
        list_score+=compute_name_score(names[ind])*(ind+1)

    return list_score

def main():
    return calc_list_score(build_name_list('names.txt'))


print main()
print time.time()-s
