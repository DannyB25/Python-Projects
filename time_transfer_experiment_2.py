# Python program to explain os.path.getmtime() method 
   
# importing os and time module 
import os
import time
import datetime
 
# Path
path = r'C:\Users\Student\OneDrive\Desktop\Customer Source'
 
# Get the time of last
# modification of the specified
# path since the epoch
modification_time = os.path.getmtime(path)
 
# convert the time in
# seconds since epoch
# to local time
local_time = time.ctime(modification_time)
print("Last modification time(Local time):", (local_time.strftime("%m-%d-%y"))

