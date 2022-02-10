"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-10 18:00:00
Title : Leap Year Program
"""

def check_four_digit_year():
    """
     Description:
         Function is used to check the input year is four digit.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the leap year.
    """  
    Year = int(input("Enter the Year: "))
    if Year>999:
           check_leap(Year)
    else:
        print("Please Enter the 4-digit Year:")
        check_four_digit_year()

def check_leap(Year):
    """
     Description:
         Function is used to check the input year or not.
     Parameter:
        No parameter required.
     Return:
         Returns nothing but prints the leap year.
    """ 
    
    if((Year % 400 == 0) or (Year % 100 != 0) and  (Year % 4 == 0)):
        print("Given Year is a leap Year")
    else:
        print ("Given Year is not a leap Year")

if __name__ == "__main__":        
    check_four_digit_year()