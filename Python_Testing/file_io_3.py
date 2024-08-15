
import os #importing os module 


fName = "Hello.txt" #giving variable a text string value 

fPath = "C:\\A\\" #giving variable a path variable. Notice the double "\\". \ is an escape sequence which tells python to ignore whatever character follows. You have to do two \\ so that it ignores the first \ but does ignore the end of our string 

abPath= os.path.join(fPath, fName)
print(abPath)

