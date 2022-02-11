"""
Author: Shreyanta Sulebhavi
Date: 2022-02-09 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 16:00:00
Title : 2D Array
"""
def two_d_matrix(m,n):
    """
    Description:
        Function is used to print 2 Dimensional Array.
    Parameter:
        m,n are used.
    Return:
        Returns Array
    """   
    arr=[]
    for i in range(m):
        rows = []
        for j in range(n):
            num = int(input(f"Enter the matrix [{i}][{j}]:"))
            rows.append(num)
        arr.append(rows)
    return(arr)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows :"))
    cols = int(input("Enter the number of columns :"))
    print(two_d_matrix(rows, cols))
