"""
Author: Shreyanta Sulebhavi
Date: 2022-02-05 10:25:00
Last Modified by: Shreyanta Sulebhavi
Last Modified time: 2022-02-11 18:00:00
Title : StopWatch Program
"""

import time

#method to convert in Hrs,Min,Sec
def time_convertor(sec):
    """
     Description:
         Function is used to calculate the time between two clicks.
     Parameter:
        Time is used.
     Return:
         Returns nothing, prints the time in hrs:min:sec
    """ 
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("total time elapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
#start time
input("Click Enter to start time: ")
start_time= time.time()
#stop time
input("Click Enter to stop time: ")
stop_time = time.time()
total_time_elapsed = stop_time - start_time

#print(total_time_elapsed)
if __name__ == "__main__":
    time_convertor(total_time_elapsed)