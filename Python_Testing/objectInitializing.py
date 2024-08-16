class name:
    def __init__(self, firstName, lastName):
        #Initializing values for future objects created from this class. gives the variable the value of itself until we define it later
        self.firstName = firstName
        self.lastName = lastName
    def printName(self):
        print("Hello, I am {} {}".format(self.firstName, self.lastName))
    
#passing in the actual object values
person = name('Dustin', 'Smith')
person.printName()
    

        
