"""
Author: Shreyanta Sulebhavi
Date: 2022-02-14 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-14 21:00:00
Title : UC2_Calculate Daily Employee Wage
"""
import random

def empWorkingHrs():
    """
    Description:
        Function is used to Check Employee is Present or Absent.
    Parameter:
        Nothing  is used.
    Return:
        Returns Employee Hours
    """  
    attendance = random.randint(0,1)
    #print(attendance)
    if attendance == 0:
        print("Employee is Absent")
        emphrs = 0
    elif attendance == 1: 
        emphrs = 8
        print("Employee is present")     
    return emphrs

def empwages(emphrs):
    """
    Description:
        Function is used to Calculate Wage Per Day.
    Parameter:
        emphrs is used.
    Return:
        Returns Employee Wages Per Day
    """
    global empRatePerHrs 
    empWagePerDay = emphrs * empRatePerHrs 
    return empWagePerDay 

if __name__ == "__main__":  
    print("Welcome to Employee Wage Computation Program")
    empRatePerHrs = 20           
    emphrs = empWorkingHrs() 
    totalEmpWage = empwages(emphrs)
    print("totalEmpWage per day is :",totalEmpWage)

