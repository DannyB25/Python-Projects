

mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def color_function(name): #define a function with a parameter
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst #returning section of function 
    

lst = color_function('Sally') #call function and pass in an argument to satisfy parameter 
for i in lst:
    print(i)


