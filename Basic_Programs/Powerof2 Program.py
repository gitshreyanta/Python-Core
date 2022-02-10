"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-10 18:00:00
Title : PowerofTwo Program
"""

def power_intput():
    """
     Description:
         Function is used to check the input power is between 0<N<31.
     Parameter:
        num is used.
     Return:
         Returns nothing.
    """ 

    num = int(input("Enter the power: "))
    if 0<= num< 31:
        pow_of_two(num)
    else:
        print("Enter value between 0 and 31")
        power_intput()

def pow_of_two(num):
    """
     Description:
         Function is used find value of Power of 2.
     Parameter:
        No parameter required.
     Return:
         Returns nothing prints power of 2 values.
    """ 
    counter = 0;
    while counter<=num:
        print(pow(2, counter))
        counter += 1

if __name__ == "__main__":
    power_intput()
