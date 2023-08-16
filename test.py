import sqlite3

connection=sqlite3.connect("Project.db")
c=connection.cursor()

#c.execute("create table customers(Username text,USN text,primary key(usn)) ")
#c.execute("delete from customers")
connection.commit()
connection.close()