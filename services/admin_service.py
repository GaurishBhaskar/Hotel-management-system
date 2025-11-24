from db import get_connection

def login(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
    result = cur.fetchone()
    conn.close()
    return result is not None
