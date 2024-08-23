from tkinter import *
import tkinter 

    
win = Tk()
win.geometry('500x170')
win.title("Check files")
b1=Button(win, width=12, height=1,text="Browse...")
b2=Button(win, width=12, height=1, text="Browse...")
b3=Button(win, width=12, height=2, text="Check for Files...")
b4=Button(win, width=12, height=2, text="Close Program...")
e1 = Entry(win, width=60)
e2 = Entry(win, width=60)
Label(win, text="").grid(row=0, column=0)
b1.grid(row=1, column=0, padx=5, pady=10)
e1.grid(row=1, column=1, padx=5, pady=10)
b2.grid(row=2, column=0, padx=5, pady=5)
e2.grid(row=2, column=1, padx=5, pady=5)
b3.grid(row=4, column=0, padx=5, pady=5, sticky="EW")
b4.grid(row=4, column=1, padx=5, pady=5, sticky="E")


