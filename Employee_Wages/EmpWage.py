"""
Author: Shreyanta Sulebhavi
Date: 2022-02-11 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-14 16:00:00
Title : UC1_Check Employee is Present or Absent
"""
import random

def empAttendance():
    """
    Description:
        Function is used Check Employee is Present or Absent.
    Parameter:
        Parameter are  not used.
    Return:
        Returns nothing
    """  
    attendance = random.randint(0,1)
    print(attendance)
    if attendance == 0:
        print("Employee is Absent")
    elif attendance == 1: 
        print("Employee is present")   

if __name__ == "__main__": 
    print("Welcome to Employee Wage Computation Program")
    empAttendance()  
