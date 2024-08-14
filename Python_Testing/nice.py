#Purpose: Demonstrating how to pass variables from function to function while
#producing a functional game. Remember, function_name(variable) _means that we
#pass in the variable. return variable _means that we are returning the variable
#back to the calling function.


def start(): #naming function
    print("Hello {}!".format(get_name())) #get name result will populate wild card and then string will be printed  

def get_name(): #naming function
    name = input("What is your name? ") #providing value to variable 
    return name #returning name to whichever function calls get_number

if __name__ == "__main__":
    start()
