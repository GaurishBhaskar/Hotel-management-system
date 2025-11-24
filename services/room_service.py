from db import get_connection

def add_room(room_number, room_type, price):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO rooms(room_number, room_type, price) VALUES (%s,%s,%s)",
                (room_number, room_type, price))
    conn.commit()
    conn.close()

def view_rooms():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM rooms")
    rooms = cur.fetchall()
    conn.close()
    return rooms
