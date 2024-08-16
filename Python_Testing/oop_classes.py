
class Game: #creating class 'game' 
    variable1 = 'Hello' #creating variable with a value 
    variable2 = 'World!' #creating variable with a value 



if __name__ == "__main__": #while module is running, it will skip code above and the commands below this line will be run
    x = Game() #creating an instance of the game class 
    print("{} {}".format(x.variable1,x.variable2)) #command to print variable 1 and variable within the game class using format method
