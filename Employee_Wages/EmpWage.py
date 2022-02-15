from email.policy import default
"""
Author: Shreyanta Sulebhavi
Date: 2022-02-14 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-14 21:00:00
Title : UC4_Solving Using Switch Case (Python Uses Dictionary concepts)
"""
import random

def empHrsForAbsent():
    """
    Description:
        Function is used to check Employee Absent.
    Parameter:
        Paramater Nothing is used.
    Return:
        Returns Employee Working Hours
    """
    emphrs = 0 
    print("Employee is Absent")
    return emphrs

def empHrsForPresent():
    """
    Description:
        Function is used to check Employee Present.
    Parameter:
        Paramater Nothing is used.
    Return:
        Returns Employee Working Hours
    """
    emphrs = 8  
    print("Employee is present")
    return emphrs  
def empHrsForHalfDay():
    """
    Description:
        Function is used to check Employee Present half day.
    Parameter:
        Paramater Nothing is used.
    Return:
        Returns Employee Working Hours
    """
    emphrs = 4
    print("Employee is present half day")
    return emphrs 

#Created a Dict for Employee Present , absent and Present halfday
empAttendance = {
    0: empHrsForAbsent,
    1: empHrsForPresent,
    2: empHrsForHalfDay
}       

def switch(attendance):
    """
    Description:
        Function is used to switch to a particular function store in dict.
    Parameter:
        attendance are used.
    Return:
        Returns Employee Per Day wage
    """    
    return empAttendance.get(attendance, default)()

def empWages(emphrs):
    """
    Description:
        Function is used to Calculate Per day Wage.
    Parameter:
        Employee Hours are used.
    Return:
        Returns Employee Per Day wage
    """
    global empRatePerHrs 
    empWagePerDay = emphrs * empRatePerHrs 
    return empWagePerDay

if __name__ == "__main__":
    print("Welcome to Employee Wage Computation Program")
    empRatePerHrs = 20 
    attendance = random.randint(0,2)
    empHrs = (switch(attendance))
    totalEmpWage = empWages(empHrs)
    print("TotalEmpWage per day is :",totalEmpWage)
    
                        


   



