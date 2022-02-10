"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-10 18:00:00
Title : PrimeFactors Program
"""
import math

def primefactors(num):
	"""
     Description:
         Function is used to calculate the prime factor of the given input
     Parameter:
        num is used.
     Return:
         Returns nothing, prints the prime factors.
    """

	for i in range(2,num + 1):
		if num % i == 0:
			count = 1
			for j in range(2,(i //2 + 1)):
				if(i % j == 0):
					count = 0
					break

			if(count == 1):
				print(i)

if __name__ == "__main__":
	num = int(input("Enter the number for prime factors :"))
	primefactors(num)
