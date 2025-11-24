from datetime import datetime
from db import get_connection

def add_booking(customer_id, room_id, check_in, check_out):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT price FROM rooms WHERE id=%s", (room_id,))
    price = cur.fetchone()[0]

    days = (check_out - check_in).days
    total_bill = days * price

    cur.execute(
        "INSERT INTO bookings(customer_id, room_id, check_in, check_out, total_bill)"
        " VALUES (%s,%s,%s,%s,%s)",
        (customer_id, room_id, check_in, check_out, total_bill)
    )
    conn.commit()
    conn.close()

def view_bookings():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT b.id, c.name, r.room_number, b.check_in, b.check_out, b.total_bill
        FROM bookings b
        JOIN customers c ON b.customer_id=c.id
        JOIN rooms r ON b.room_id=r.id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
