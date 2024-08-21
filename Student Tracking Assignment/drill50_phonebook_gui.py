from tkinter import * #importing tkinter and its modules 
import tkinter as tk
from tkinter import messagebox

#be sure to import out other modules so we can have access to them
import drill50_phonebook_main
import drill50_phonebook_func

def load_gui(self): #defining a function with the self that gives access to class (parentwindow) objects

    self.lbl_fname = tk.Label(self.master,text='First Name:') #calling tkinter's class for label, accessing it and instantiating it (lbl_fname). Also placing it in window and giving it the text 'First Name'
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W) #places label above using grid. 
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = tk.Label(self.master,text='Current Course:')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_user = tk.Label(self.master,text='User:')
    self.lbl_user.grid(row=0, column=2, padx=(0,0), pady=(10,0), sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text='') #creating area for users to input text through tk class for entry. this line is for first name 
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W) #this is placement for the first name entry area 
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))#creating an event listener (bind) to our list box so that if a user clicks the box it will run the function (phonebook_func.onSelect)
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: drill50_phonebook_func.addToList(self)) #creating button through tk class Button
    self.btn_add.grid(row=10,column=0,padx=(25,0),pady=(45,10),stick=W) #placement of button 
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: drill50_phonebook_func.onUpdate(self))
    self.btn_update.grid(row=10,column=1,padx=(15,0),pady=(45,10),stick=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: drill50_phonebook_func.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(15,0),pady=(45,10),stick=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: drill50_phonebook_func.ask_quit(self))
    self.btn_close.grid(row=10,column=4,columnspan=1,padx=(15,0),pady=(45,10),stick=E)

    drill50_phonebook_func.create_db(self)#calling phonebook function to create database
    drill50_phonebook_func.onRefresh(self) #calling phonebook function to run onRefresh function 

if __name__ == "__main__":
    pass  #this passes or doesn't run anything. Everything will be run through the phonebook_main source code 

    



    
