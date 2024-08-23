# Python program to explain os.path.getmtime() method 
   
# importing os, time and sys module 
import os
import sys
import time
import datetime 
 
# Path
path = r'C:\Users\Student\OneDrive\Desktop\Customer Source'

#Destination
bound= r'C:\Users\Student\OneDrive\Desktop\Customer Destination'
 
# Get the time of last
# modification of the specified
# path since the epoch
try:
    modification_time = os.path.getmtime(path)
    print("Last modification time since the epoch:", modification_time)
 
except OSError:
    print("Path '%s' does not exists or is inaccessible" %path)
    sys.exit()
 
# convert the time in
# seconds since epoch
# to local time
local_time = time.ctime(modification_time)
print("Last modification time(Local time):", local_time)
 
 
# above code will print
# path does not exists or is inaccessible'
# if the specified path does not
# exists or is inaccessiblex = datetime.datetime(now)
x=datetime.datetime.now()
print(x.strftime("%c"))
print(x.strftime("%m-%d-%y-%H-%M-%S"))
y=datetime.date.today()
print(y)

today = datetime.date.today()


print("Today:", today)

      
