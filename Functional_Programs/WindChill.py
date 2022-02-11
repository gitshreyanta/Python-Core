"""
Author: Shreyanta Sulebhavi
Date: 2022-02-09 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 16:00:00
Title : WindChill
"""
import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))

if t<50:
    if v>120 or v<3:
        wci = 13.12 + 0.6215 * t - 11.37 * math.pow(v, 0.16) + 0.3965 * t * math.pow(v, 0.16)
        print("The wind chill index is", int(round(wci, 0)))
    else:
        print("please enter the wind speed greater than 120 or less than 3: ")
else:
    print("Please enter the temperatue less than 50")





