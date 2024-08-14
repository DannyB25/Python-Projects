#Purpose: Demonstrating how to pass variables from function to function while
#producing a functional game. Remember, function_name(variable) _means that we
#pass in the variable. return variable _means that we are returning the variable
#back to the calling function.

import pygame #import pygame for sound effect 

pygame.init() #initializing/calling pygame

pygame.mixer.init() #initializing/calling mixer 

def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name) #describe_name function, providing argument of name
    nice,mean,name = nice_mean(nice,mean,name) #creating function and providing arguments

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player
        for playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name

    if name != "": #this basically asks if the name variable is empty or not. if not empty print statement below or move to else (!= means not equal to)
        print("\nThank you for playing again, {}!".format(name))
    else: #if the if statement is false. proceed with code below 
        stop = True #giving variable stop variable the value of true 
        while stop: #if stop is true proceed with code below 
            if name == "": #if name is empty go to next 
                name = input("\nWhat is your name? \n>>> ").capitalize() #ask what their name is, provide input ability and capitalize their response
                if name != "": #if name is not empty go to message below
                    print("\nWelcome, {}!".format(name))#plugs name into wild card 
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False #if we have their name, this stops the function from repeating 
    return name #returns name value to describe_game function, which is also provided to start function 

def nice_mean(nice,mean,name): # creating function with three arguments provided 
    stop = True #assigning stop variable the value of True
    while stop: #while stop is true, do the loop below 
        show_score(nice,mean,name) #function created with arguments provided  
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()#gives user the input to provide response and then lower cases the response 
        if pick == "n": # if user picks the "n" value, print message below and add +1 to nice 
            print("\nThe stranger walks away smiling...") #message to print if "n" is picked 
            nice = (nice + 1) #adds +1 to nice 
            stop = False #stops the previous loop 
        if pick == "m": #if user provides m, print message below and add + 1 to mean 
            print("\nThe stranger glares at you \nmenacingly and storms off...") #message to print if "m" is provided by user
            mean = (mean + 1) #adding +1 to mean tally 
            stop = False #stops loop 
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name): #define function and provide three arguments 
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))#message that shows score of the game

def score(nice,mean,name):
    #score function is being passed the values stored with the 3 variables
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        #else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

win_sfx = pygame.mixer.Sound("win.mp3") #variable defined with sound effect
lose_sfx = pygame.mixer.Sound("lose.mp3") #variable defined with sound effect 


def win(nice,mean,name):
    win_sfx.play()#command to play sound effect 
    #substitue the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name): #define function and provide arguments
    lose_sfx.play()#command to play sound effect 
    #Substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)#calling again function 

def again(nice,mean,name): #define function and providing arguments
    stop = True #provide stop True value 
    while stop: #while true, perform the next loop 
        choice = input("\nDo you want to play again? (y/n): \n>>> ").lower() #input for user to decide if they want to play again. lower case the response 
        if choice == "y": #if user chooses y 
            stop = False #stop the loop
            reset (nice,mean,name)#call reset function 
        if choice == "n": #if user chooses no 
            print("\nOh, so sad, sorry to see you go!")#print this message 
            stop = False #stop loop 
            quit() #call quit function 
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ") #if a y or n not provided, restates question with this message

def reset(nice,mean,name): #defining function with arguments
    nice = 0 #give nice variable a 0 value
    mean = 0 #give mean variable a 0 value 
    #notice, I do not reset the name variable as that same user has elected to play again 
    start(nice,mean,name)#call start function

    
if __name__ == "__main__":
    start()
