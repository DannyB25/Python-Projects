class Protected: #creating class 
    def __init__(self): #creating init function 
        self.__privateVar = 5 #providing values to variable 
        self._protectVar = 10 #providing values to variable 

    def getPrivate(self): #creating a new function 
        print(self.__privateVar) #command to print out privateVar function 
    def getProtect(self): #creating a new function 
        print(self._protectVar) #command to print protectVar function 
    def setPrivate(self,private): #creating a new function 
        self.__privateVar = private #setting the value of private to self.__privateVar
    def setProtect(self,private_two): #creating a new function 
        self._protectVar = private_two #setting the value of private_two to self._protectVar

obj = Protected() #giving obj variable equal to Protected function.
obj.getPrivate() #command to run function
obj.getProtect() #command to run function
obj.setPrivate(24) #command to run function w/ value provided
obj.getPrivate() #command to run function
obj.setProtect(50) #command to run function w/ value provided 
obj.getProtect() #command to run function

    
    
