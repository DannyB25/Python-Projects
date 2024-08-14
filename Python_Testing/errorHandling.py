
def getInfo(): #naming function
    var1 = input("\nPlease provide the first numeric value: ") #input method gathers info from a user. in this case it is put into the attached variable var1
    var2 = input("\nPlease provide the second numeric value: ")
    return var1, var2 #returns these two variables to getInfo below
    #compute(var1,var2) #calling function with two arguments. 

def compute():
    go = True
    while go:
        var1, var2 = getInfo() #calls get info function and 
        try: #try is our first attempt at completing this function 
            var3 = int(var1) + int(var2) #int changes users input into a integer as all user input is default text/string value
            #print("{} + {} = {}".format(var1, var2, var3)) #prints three values using the format method to plug in 3 variables
            go = False #will turn off the code remaining if try is successful
        except ValueError as e: #as e is the variable for ValueError which will print before our string. if try doesn't work/gets value error, move to except process which will print error message from computer and the written string below
            print("{}: \n\nYou did not provide a numeric value!".format(e))
        except: # this will display the below string if the try and except don't work
            print("\n\nOops, you provided invaled input, program will close now!")
        """finally: #this will run at the end of this function no matter what after everything above is completed 
            print("Moving on...")"""
    print("{} + {} = {}".format(var1, var2, var3))


if __name__ == "__main__": #this means if this module is being ran do code underneath...
    compute() #calls function
