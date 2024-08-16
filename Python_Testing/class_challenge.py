

class Basketball: #Creating a class
    def __init__(self,time,players,teams): #creating a init function for assigning values 
        self.time=time #assigning variables to objects 
        self.players=players
        self.teams=teams
    def rules(self): #new function 
        #message to be produced using init/value placement 
        print("A basketball game is {} minutes long and has {} players on the \
court belonging to {} separate teams.".format(self.time,self.players,self.teams))

figures = Basketball("60","10","2")
figures.rules()
    
    
