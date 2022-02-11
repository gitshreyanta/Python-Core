"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 15:00:00
Title : CouponNumber Program
"""
import random
"""
     Description:
         Function is used to find the Given N distinct Coupon Numbers.
     Parameter:
        Random is used.
     Return:
         Returns the random Coupon Number.
""" 
def coupon_numbers(x):
    num = '0123456789'
    coupon_num = ''
    for i in range(0, x):
        x = random.randint(0, len(num) - 1)
        coupon_num += num[x: x + 1]
    return coupon_num

if __name__ == "__main__":
    number = int(input("Enter the Coupon Number length :"))
    print(coupon_numbers(number))