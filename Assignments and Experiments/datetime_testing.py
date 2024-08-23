
from datetime import datetime
from datetime import *
import pytz


newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")

londonTz = pytz.timezone("Europe/London") 
timeInLondon = datetime.now(londonTz)
currentTimeInLondon = timeInLondon.strftime("%H:%M:%S")

PortlandTz = pytz.timezone("America/Los_Angeles") 
timeInPortland = datetime.now(PortlandTz)
currentTimeInPortland = timeInPortland.strftime("%H:%M:%S")

print("The current time in New York is:", currentTimeInNewYork)
print("The current time in London is:", currentTimeInLondon)
print("The current time in Portland is:", currentTimeInPortland)

l= currentTimeInLondon
n= currentTimeInNewYork[:2]#[:2] provides only the first two characters in your argument
p=currentTimeInPortland[:2]#[:2] provides only the first two characters in your argument

if int(l) > 17:
        print("The London branch is closed!")
elif int(l) < 9:
        print("The London branch is closed!")
else:
    print("The London branch is open!")

if int(n) > 17:
        print("The New York branch is closed!")
elif int(n) < 9:
        print("The New York branch is closed!")
else:
    print("The New York branch is open!")

if int(p) > 18:
        print("The Portland branch is closed!")
elif int(p) < 9:
        print("The Portland branch is closed!")
else:
    print("The Portland branch is open!")

import datetime
x = datetime.datetime.now()
print(x)
