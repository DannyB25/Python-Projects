import tkinter as tk #importing modules 
from tkinter import *
import webbrowser #this module allows creating of web browsers through Python

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #the line below creates a button that will send user to a web browser. the command makes it so when the user presses the button the defaultHTML function runs 
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #the line below is the placement for the button we created above
        self.btn.grid(row= 3, column= 4, padx=(10,10) , pady=(10,10), sticky='e')
        #the following line creates a button for user to submit text they wrote to a website. the command makes it so when the user presses the button the userHTML function runs 
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.userHTML)
        #the following line is for the placement of the user submit button above
        self.btn.grid(row =3, column = 5, padx=(10,10) , pady=(10,10), sticky='e')
        #the line below creates an entry for users to type in text. 
        self.user_submit = Entry(width=100)
        #the following line is the placement of the entry for user input 
        self.user_submit.grid(row=1, column=0, columnspan=6, padx=(5,5), pady=(20,5))
        #calling tkinter's class for label, accessing it and instantiating it (lbl_fname). Also placing it in window and giving it the text 'First Name'
        self.lbl_user = tk.Label(self.master,text='Enter custom text or click the Default HTML page button:')
        #placement for label above the text box/user entry
        self.lbl_user.grid(row=0,column=1,padx=(10,0),pady=(10,0),sticky=N+W)
    def defaultHTML(self):
        htmlText= "Stay tuned for our amazing summer sale!" #default text on the page 
        htmlFile = open("index.html", "w") #This opens the web browswer. w creates file if one doesn't exist. 
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>" #creates html template, places htmlText variable in the body
        htmlFile.write(htmlContent)#commands the creation of the website via the opening of web browser and filling it with the two variables mentioned
        htmlFile.close()#closes website
        webbrowser.open_new_tab("index.html")#opens browser in a new tab 
    def userHTML(self):
        customText= self.user_submit.get() #this allows user input to be added to the site via the get() fucntion
        htmlFile = open("index.html", "w") #opens web browser. w creates the file if it doesn't exist yet 
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>" #creates html template and places customText variable inside body of html page
        htmlFile.write(htmlContent)#writes the htmlContent variable within the open web page
        htmlFile.close()#closes browser 
        webbrowser.open_new_tab("index.html")#opens browser in a new tab

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
