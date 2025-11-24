from db import get_connection

def add_customer(name, phone, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO customers(name, phone, email) VALUES (%s,%s,%s)", 
                (name, phone, email))
    conn.commit()
    conn.close()

def view_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    conn.close()
    return rows

