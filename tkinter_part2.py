
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

        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray' ) #instantiating label object for first name 
        self.lblFName.grid(row=0,column=0,padx=(30,0),pady=(30,0))#determing where we are placing the label using the grid manager. This will place label in upper left corner.
        #padx give padding on the x axis, pady gives padding on the y axis

        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray' ) #instantiating label object for first name 
        self.lblLName.grid(row=1,column=0,padx=(30,0),pady=(30,0))#determing where we are placing the label using the grid manager. This will place label one row down from upper left corner 

        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))
        
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue') #calling the entry widget from tkinter.
        #This will provide a text box in the self master which is the entire frame. Then we are making the text equal to the varfname and then providing the font
        #font size, and a color for the foreground and background. This is instantiating this object
        self.txtFName.grid(row=0,column=1,padx=(30,0),pady=(30,0)) #paints txtFName onto window. FYI colspan= would allow you to span multiple columns with your image

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue') #same as above but with varLName
        self.txtLName.grid(row=1,column=1,padx=(30,0),pady=(30,0)) #same as above but with txtLName

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) #creating submit button with the "submit" text overtop, the width equal to 10 pixels, height equal to 2 pixels. command is what happens when button is clicked and self.submit is the function that will handle that action
        self.btnSubmit.grid(row=2,column=1,padx=(0,0),pady=(30,0), sticky=NE)#where we want button to stick (NE=NorthEast or up and to the right)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel) #creating cancel button with the "cancel" text overtop, the width equal to 10 pixels, height equal to 2 pixels
        self.btnCancel.grid(row=2,column=1,padx=(0,90),pady=(30,0), sticky=NE)#where we want button to stick (NE=NorthEast or up and to the right)

    def submit(self): #method creation. self = class, submit is the method
        fn = self.varFName.get() #variable that will store values. self.varFName has the value. .get is what returns the value
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln)) #output for label. config() changes something dynamically while program is running 
        

    def cancel(self): #method creation. self = class, cancel is the method 
        self.master.destroy() #this will close the window if someone clicks cancel. destroy() closes it 
            
 




if __name__ == "__main__": #if module is running, calls commands below this
    root = Tk() #instantiate tkinter, naming it root
    App = ParentWindow(root) #passing to our class program 
    root.mainloop() #used to keep programming running 
