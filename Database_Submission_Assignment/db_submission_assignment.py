import sqlite3 #import sqlite3 module 

conn = sqlite3.connect('new.db') #assigning the connect to sqlite3 method to variable conn
with conn: #with connection to db running 
    cur = conn.cursor() #variable value is the activation of the cursor which can implement commands into db
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_title STRING)") #this creates the table tbl_files and the two columns within that table 
    conn.commit() #commits the changes implemented above

    
conn = sqlite3.connect('new.db') #connecting to db

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg') #creating variable which will store the file name tuple

for locate in fileList: #for loop and variable locate activated. So loop into the fileList...
    if locate.endswith('.txt'): #if statement created. if a value ends in our tuple ends in .txt... 
        with conn: #while connected to db
            cur = conn.cursor() #adding variable cur which is assigned the value of activating the cursor which can implement our commands into the db
            cur.execute("INSERT INTO tbl_files (col_title) VALUES (?)", (locate,)) #this inserts the values into the col_title the files that we found to end in .txt
            print(locate) #this prints the result of locate

conn.close() #this closes the connection to the database (db)
