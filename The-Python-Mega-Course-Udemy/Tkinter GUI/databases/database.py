import psycopg2
def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='12@Postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='12@Postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='12@Postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows
#print(view())

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='12@Postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='12@Postgres' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

#print(view())
#delete_all()
create_table()
insert_data("Water Glass", 10, 5)
insert_data("Orange", 100, 30)
insert_data("Apples", 20, 35)
# delete("Water Glass")
# delete("Orange")
# delete("Apples")
update(11, 6, "Water Glass")
print(view())
