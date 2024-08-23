
import tkinter #import tkinter
from tkinter import * #code to be able to access all of tkinter's widgets 


class ParentWindow(Frame): #creating class w/ frame object 
    def __init__ (self, master): #function of initializing values 
        Frame.__init__ (self) #initializing values for frame object 

        self.master = master #this is code to create a window frame for the user 
        self.master.resizable(width=False, height=False) #this says we cannot resize the screen. If we changed false to true, we could resize the height and width
        self.master.geometry('{}x{}'.format(700,400)) #sets the pixels of the grame 
        self.master.title('Learning Tkinter!') #this sets what to display at the top of the web page 
        self.master.config(bg='lightgray') #this sets the color of the background of the screen

        self.varFName = StringVar() #instantiated objects and passed it over to variable 
        self.varLName = StringVar() #instantiated objects and passed it over to variable
        
        """self.varFName.set('Bob') #setting (or giving) the value for variable.
        self.varLName.set('Smith') #setting (or giving) the value for variable.

        print(self.varFName.get()) #this gets/retrieves the value we plugged in for this variable 
        print(self.varLName.get()) #this gets/retrieves the value we plugged in for this variable"""

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue') #calling the entry widget from tkinter.
        #This will provide a text box in the self master which is the entire frame. Then we are making the text equal to the varfname and then providing the font
        #font size, and a color for the foreground and background. This is instantiating this object
        self.txtFName.pack() #paints txtFName onto window

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue') #same as above but with varLName
        self.txtLName.pack() #same as above but with txtLName
        
 




if __name__ == "__main__": #if module is running, calls commands below this
    root = Tk() #instantiate tkinter, naming it root
    App = ParentWindow(root) #passing to our class program 
    root.mainloop() #used to keep programming running 
