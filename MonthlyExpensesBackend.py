# importing library
import sqlite3

# creating table if not exist
def connect():
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expenses (id integer PRIMARY KEY NOT NULL, item text NOT NULL, amount real NOT NULL, year integer NOT NULL, monthname text NOT NULL)")
    conn.commit()
    conn.close()

def insert(item,amount,year,monthname):
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO expenses VALUES(NULL,?,?,?,?)",(item,amount,year,monthname))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(item="",amount="",year="",monthname=""):
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM expenses WHERE item=? OR amount=? or year=? OR monthname=?",(item,amount,year,monthname))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,item,amount,year,monthname):
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("UPDATE expenses SET item=?, amount=?, year=?, monthname=? WHERE id=?",(item,amount,year,monthname,id))
    conn.commit()
    conn.close()
    
connect()
#insert("Wheat",899,2018,"October")
#delete(2)
#update(1,"Rice",1000,2018,"October")
print(view())
#print(search(item="Rice"))

