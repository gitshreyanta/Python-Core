"""
Author: Shreyanta Sulebhavi
Date: 2022-02-14 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-14 21:00:00
Title : UC3_Check add Part time Employee & Wage
"""
import random

def empWorkingHrs():
    """
    Description:
        Function is used to check Employee Present Absent & Half Day.
    Parameter:
        Nothing is used.
    Return:
        Returns Employee Hours
    """
    attendance = random.randint(0,2)
    #print(attendance)
    if attendance == 0:
        print("Employee is Absent")
        emphrs = 0
    elif attendance == 1: 
        emphrs = 8
        print("Employee is present")   
    elif attendance == 2:
        emphrs = 4
        print("Employee is present half day")    
    return emphrs

def empWages(emphrs):
    global empRatePerHrs 
    """
    Description:
        Function is used to Calculate Per day Wage.
    Parameter:
        Employee Hours are used.
    Return:
        Returns Employee Per Day wage
    """
    empWagePerDay = emphrs * empRatePerHrs 
    return empWagePerDay 

if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    empRatePerHrs = 20             
    emphrs = empWorkingHrs() 
    totalEmpWage = empWages(emphrs)
    print("totalEmpWage per day is :",totalEmpWage)

