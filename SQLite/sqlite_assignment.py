import sqlite3
connection=sqlite3.connect(r"C:/Users/Student/OneDrive/Documents/GitHub/Python-Projects/SQLite/test_database.db")
c=connection.cursor()
c.execute("CREATE TABLE People(FirstName Text, LastName TEXT, Age INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious',42)")
connection.commit()
