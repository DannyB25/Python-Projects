from abc import ABC, abstractmethod #importing modules 
class purchase(ABC):  #creating class with argument passed in
    def restriction(self,amount): #creating function w/ arguments 
        print("You've set your maximum payment to: ",amount) #print command 
    @abstractmethod #here we start abstracting. provides a function without giving any values or implementation details for the arguments 
    def itemCost(self,amount): #creating function with arguments
        pass #this says to not run anything 

class checkPayment(purchase): #creating class w/ purchase class as argument 
    def itemCost(self,amount): #creating function with arguments 
        print('Your purchase amount of {} exceeds your $1,000.00 limit '.format(amount)) #print command with amount variable plugged in 

obj = checkPayment() #variable obj is equal to the class checkPayment 
obj.restriction("$1,000.00") #calling restriction function 
obj.itemCost("$2,000.00") #calling itemCost function 

