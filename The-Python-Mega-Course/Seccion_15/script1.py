import sqlite3

def create_table():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)")
    con.commit()
    con.close()

def insert(item, quantity, price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows =cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete(item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    con.commit()
    con.close()

def update(quantity, price, item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    con.commit()
    con.close()


update(20,6,"Wine Glass")
rows = view()

for row in rows:
    print(row)
