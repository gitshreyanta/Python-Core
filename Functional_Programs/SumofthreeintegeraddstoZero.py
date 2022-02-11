"""
Author: Shreyanta Sulebhavi
Date: 2022-02-09 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 16:00:00
Title : Sum of three Integer adds to ZERO
"""


def triplet(num, arr):
    """
     Description:
         Function is used to find the number of distinct triplets whose sum is 0.
     Parameter:
        Number and array are used.
     Return:
         Returns nothing, prints the triplets
    """

    for i in range(0, num-2):
        for j in range(i+1, num-1):
            for k in range(j+1, num):
                if arr[i] + arr[j] + arr[k] == 0:
                    print("sum of these triplets is 0: ", arr[i] , arr[j] , arr[k])

if __name__ == "__main__":
    num = int(input("Enter the number of elements:"))

    arr=[]
    for i in range(num):
        arr.append(int(input("Enter each element:")))
    triplet(num, arr)