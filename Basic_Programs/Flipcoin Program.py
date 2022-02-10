"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-10 18:00:00
Title : flipcoin Program
"""
import random
import itertools

def flip_coin(num):
    """
     Description:
         Function is used to calculate the head and tail count for a given number of flips.
     Parameter:
        num is used.
     Return:
         Returns nothing but prints the percentage of head and tail.
    """    

    tail_count = 0
    head_count = 0

    for i in range(num):
        flip = random.uniform(0,1)
        #print(flip)
        if flip > 0.5 :
            head_count +=1
        else:
            tail_count +=1

    print('Head Percentage:',(head_count / num)*100 )
    print('Tails Percentage:',(tail_count / num)*100 )

if __name__ == "__main__":
    num = int(input("Please Enter The number of times to Flip Coin:"))
    flip_coin(num)

