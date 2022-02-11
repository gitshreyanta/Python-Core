"""
Author: Shreyanta Sulebhavi
Date: 2022-02-09 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 16:00:00
Title : Distance of lines
"""
import math
def length_line(x,y):
    """
     Description:
         Function is used to calculate length of line for given point from origin.
     Parameter:
        x,y are used.
     Return:
         Returns length of line
    """
    length = math.sqrt((x * x) + (y * y))
    return length

if __name__ == "__main__":
    x = float(input("Enter the 1st co-orinate x: "))
    y = float(input("Enter the 2nd co-orinate y: "))
    print(length_line(x,y))