'''Project Euler #14
The following iterative sequence is defined for the set of positive integers:

n->n/2 (n is even)
n->3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13->40->20->10->5->16->8->4->2->1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
def next_term(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def find_max_Collatz_chain(N):

    max_length = 1
    max_length_n = 1
    chain_length_dict = {1:1}

    ii = 2

    while ii<N:
        cur_n = ii
        chain_length = 1
        while cur_n>1:
            cur_n = next_term(cur_n)

            if cur_n in chain_length_dict:
                chain_length+=chain_length_dict[cur_n]
                break
        
            chain_length+=1

        chain_length_dict[ii]=chain_length

        if chain_length>max_length:
            max_length = chain_length
            max_length_n = ii
        ii+=1

    return [max_length_n, max_length]

def main():
    return find_max_Collatz_chain(1000001)[0]
