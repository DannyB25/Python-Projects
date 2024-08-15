#the purpose of this code is to iterate through the C:\B folder and produce only the files that have the ".txt" extension. Also, provide the date/time the files were
#last modified. 

import os #import os module 
import time #import time module 
from datetime import datetime #from the datetime library, we import the date time module 

fPath = "C:\\B\\" #giving variable a value. This is the file path to the folder to be examined

textFiles = "seven.txt"

def theDirectory(): #defining the function 
    directory = os.listdir(fPath) #creating variable. using listdir method to layout files in the directory 
    print(directory) #print command of variable which is the directory mentioned above
    for fileName in directory: #for loop with created variable fileName to go through the directory 
        if fileName.endswith(".txt"): #if condition using the endswith function to weed out files with .txt at the end in the directory. Only outputs .txt files 
            thePath = os.path.join(fPath, fileName) #produces absolute path for the directory using the fileName variable which has excluded everything but .txt files  
            modTime = os.path.getmtime(thePath) #produces the date/time for everything within thePath (which has produced an absolute path for files with .txt at the end
            print(thePath + "-" + str(datetime.fromtimestamp(modTime))) #printing the output of thePath, adding a hyphen, and the producing the date while converting it to timestamp format 
    
theDirectory()

"""
def absolutePath():
    thePath = os.path.join(fPath, textFiles)
    print(thePath)

absolutePath()

def fileCreate():
    modTime = os.path.getmtime(fPath)
    print(modTime)

fileCreate()
"""
