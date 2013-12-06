'''Project Euler #58

Julie proposes the following wager to her sister Louise.
She suggests they play a game of chance to determine who will wash the dishes.
For this game, they shall use a generator of independent random
numbers uniformly distributed between 0 and 1.
The game starts with S = 0.
The first player, Louise, adds to S different random
numbers from the generator until S > 1 and records her
last random number 'x'.

The second player, Julie, continues adding to S different random numbers
from the generator until S > 2 and records her last random number 'y'.
The player with the highest number wins and the loser washes the
dishes, i.e. if y > x the second player wins.

For example, if the first player draws 0.62 and 0.44, the first
player turn ends since 0.62+0.44 > 1 and x = 0.44.
If the second players draws 0.1, 0.27 and 0.91, the second player
turn ends since 0.62+0.44+0.1+0.27+0.91 > 2 and y = 0.91. Since y > x,
the second player wins.

Louise thinks about it for a second, and objects: "That's not fair".
What is the probability that the second player wins?
Give your answer rounded to 10 places behind the decimal point in the
form 0.abcdefghij
'''

import mwmath
import random
import time


def player_turn(starting_pt):
    cur_score = starting_pt
    if starting_pt == 0:
        final_score = 1000000
    else:
        final_score = 2000000
        
    while cur_score<final_score:
        last_val = random.randint(1,1000000)
        cur_score =  cur_score + last_val
    
    return [cur_score,last_val]

def run_game():
    A = player_turn(0)
    B = player_turn(A[0])
    
    if A[1]>B[1]:
        return 0
    else:
        return 1

def main(N):
    B_wins = 0

    for ii in range(N):
        B_wins = B_wins + run_game()

    return (1.0*B_wins)/N

t = time.time()
print main(630948938)
print time.time()-t
