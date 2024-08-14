mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name): #define a function with a parameter
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst #returning section of function

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("You need to provide your name!")
        elif name == 'Sally':
            print("Sally, you may not use this software.")
        else:
            go = False
        
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()


def thine_Function():
    print("hello, there!")

thine_Function()

def ano_Function(fname): #define function, provide a parameter
    print(fname + "King")

ano_Function("BB") #providing argument to function (bb king)
ano_Function("Earl") #providing argument to function (earl king)
ano_Function("Albert") #providing argument to function


jobs = ["construction", "tech", "psychiatrist", "geologist"] # an array

for alphabet in jobs: #looping through the jobs array using for in loop 
    print(alphabet)

l = jobs.count("construction") #count method tells you the number of times a value appears in an array
print(l)

jobs.sort() #sort method alphabetizes the array 
print(jobs)

derka = lambda o, u : o * u # this is an example of an anonymous function; can take any number of arguments but only one expression 
print(derka(4, 8))



    
    


    
