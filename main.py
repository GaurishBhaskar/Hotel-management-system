from services.admin_service import login
from services.room_service import add_room, view_rooms
from services.customer_service import add_customer, view_customers
from services.booking_service import add_booking, view_bookings
from datetime import datetime

def admin_panel():
    while True:
        print("\n--- ADMIN DASHBOARD ---")
        print("1. Manage Rooms")
        print("2. Manage Customers")
        print("3. Manage Bookings")
        print("0. Logout")
        ch = input("Enter choice: ")

        if ch == '1':
            print("\n1. Add Room\n2. View Rooms")
            sub = input("Choice: ")
            if sub == '1':
                rn = input("Room No: ")
                rt = input("Type (Single/Double/Suite): ")
                price = float(input("Price per night: "))
                add_room(rn, rt, price)
                print("Room added!")
            elif sub == '2':
                for r in view_rooms():
                    print(r)

        elif ch == '2':
            print("\n1. Add Customer\n2. View Customers")
            sub = input("Choice: ")
            if sub == '1':
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                add_customer(name, phone, email)
                print("Customer added!")
            elif sub == '2':
                for c in view_customers():
                    print(c)

        elif ch == '3':
            print("\n1. Add Booking\n2. View Bookings")
            sub = input("Choice: ")
            if sub == '1':
                cid = int(input("Customer ID: "))
                rid = int(input("Room ID: "))
                ci = datetime.strptime(input("Check-in (YYYY-MM-DD): "), "%Y-%m-%d").date()
                co = datetime.strptime(input("Check-out (YYYY-MM-DD): "), "%Y-%m-%d").date()
                add_booking(cid, rid, ci, co)
                print("Booking done!")
            elif sub == '2':
                for b in view_bookings():
                    print(b)

        elif ch == '0':
            break

if __name__ == "__main__":
    print("=== HOTEL MANAGEMENT SYSTEM ===")
    u = input("Username: ")
    p = input("Password: ")
    if login(u, p):
        admin_panel()
    else:
        print("Invalid login!")
