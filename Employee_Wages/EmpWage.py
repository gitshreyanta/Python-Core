"""
Author: Shreyanta Sulebhavi
Date: 2022-02-14 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-14 21:00:00
Title : UC5_Calculating Wages for a Month(Assume 20 Working Day per Month)
"""
import random

def empWorkingHrs():
    """
    Description:
        Function is used to Check Employee is Present or Absent and Half day and Calculate working days.
    Parameter:
        nothing  is used.
    Return:
        Returns Employee Hours and Total Working Days
    """ 
    global totalWorkingDays 
    attendance = random.randint(0,2)
    #print(attendance)
    if attendance == 0:
        #print("Employee is Absent")
        empHrs = 0
        totalWorkingDays = totalWorkingDays + 1
    elif attendance == 1: 
        empHrs = 8
        totalWorkingDays = totalWorkingDays + 1
        #print("Employee is present")   
    elif attendance == 2:
        empHrs = 4
        totalWorkingDays = totalWorkingDays + 1
        #print("Employee is present half day")    
    return empHrs,totalWorkingDays

def empWages(emphrs):
    """
    Description:
        Function is used to Calculate employee Rate Per Day.
    Parameter:
        Employee Hours is used.
    Return:
        Returns Employee Wage per Day
    """ 
    global empRatePerHrs
    empWagePerDay = emphrs * empRatePerHrs
    return empWagePerDay 

if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    totalWorkingDays = 0
    numOfWorkingDays = 20
    empRatePerHrs = 20
    totalEmpHrs = 0
    while (totalWorkingDays < numOfWorkingDays):            
        empHrs, totalWorkingDays = empWorkingHrs() 
        totalEmpHrs = totalEmpHrs + empHrs
    
    #perDayEmpWage = empWages(empHrs)
    totalEmpWage = empWages(totalEmpHrs)
    print("TotalWorking Hrs Per Month is :", totalEmpHrs)
    print("TotalEmpWage per month is :",totalEmpWage)

