"""
Author: Shreyanta Sulebhavi
Date: 2022-02-09 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 16:00:00
Title : Quadratic Equation
"""
import math

def equationroots(a, b, c):
    """
     Description:
         Function is used to find the two roots of Quadratic equation .
     Parameter:
        a,b,c are used.
     Return:
         Returns nothing, prints roots.
    """

    delta = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(delta))


    if delta > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif delta == 0:
        print(" real and same roots")
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

if __name__ == "__main__":
    a = int(input("Enter the constant a:"))
    b = int(input("Enter the constant b:"))
    c = int(input("Enter the constant c:"))

    if a == 0:
        print("Input correct quadratic equation")
    else:
        equationroots(a, b, c)
