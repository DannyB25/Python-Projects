
import app #allows access to the app file/module

def print_app2(): #defining function 
    name = (__name__) #this will pull the file app.py 
    return name

if __name__ == "__main__": #== is an equal comparison that says if both sides are the same, run the script below#

# __main__ is the script being run when you perform the run module

    #the following is calling code from within this script
    print("I am running code from {}".format(print_app2()))

    #the following is calling code from within the imported app.py
    print("I am running code from {}".format(app.print_app()))

