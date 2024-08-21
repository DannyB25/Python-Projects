#purpose: this is a phonebook demo which demonstrates OOP, Tkinter GUI module,
#using Tkinter parent and child relationships.


#import tkinter and other modules 

import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter as tk

import drill50_phonebook_gui
import drill50_phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame): #creating class of ParentWindow and associating w/ Tkinter Frame 
    def __init__(self, master, *args, **kwargs): #initializing values. self references class and master references frame 
        Frame.__init__(self, master, *args, **kwargs) #

        #define our master frame configuration
        self.master = master #allows access to frame (master). self.master is the address for that access basically 
        self.master.minsize(500,300) #(Height, Width). setting the minimum size dimensions  
        self.master.maxsize(500,300) #setting the maximum size dimensions 
        #This CenterWindow method will center our app on the user's screen 
        drill50_phonebook_func.center_window(self,500,300) #accessing phonebook_func script (we have imported it above) and then centering our window and providing dimensions
        self.master.title("The Tkinter Phonebook Demo") #referencing the class and frame and creating the title for our window 
        self.master.configure(bg="#F0F0F0") #creating a background color for our window  
        # This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self)) #basically closes program when the x in the right hand corner is clicked 

        #load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        drill50_phonebook_gui.load_gui(self)



if __name__ == "__main__": #if module/script is run, perform the code below 
    root = tk.Tk() #syntax to create window from Tkinter
    App = ParentWindow(root) #feeding our class into the App variable and adding root which is the window we created in the line above 
    root.mainloop() #this keeps the window open until we decide to close the loop 
                              
