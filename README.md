# Hotel Management System (Python + MySQL)

A console-based Hotel Management System built using **Python** and **MySQL**, redesigned for clean project structure and GitHub portfolio presentation.

---

## 🚀 Features

✔ Admin Login (Default: `admin/admin123`)  
✔ Manage Rooms  
✔ Manage Customers  
✔ Manage Bookings  
✔ Auto Bill Calculation  
✔ SQL Database Integration  
✔ Organized Modular Code Structure  

---

## 🛠️ Tech Stack

- **Python**
- **MySQL Database**
- File Handling / CRUD Operations
- Modular Programming Structure

---

## 📂 Project Structure

Hotel-Management-System/
│ README.md
│ config.py
│ db.py
│ main.py
│ requirements.txt
│ schema.sql
│
├─ models/
│ ├ booking.py
│ ├ customer.py
│ └ room.py
│
└─ services/
├ admin_service.py
├ booking_service.py
├ customer_service.py
└ room_service.py

---

## 🔧 How to Run

1️⃣ Install MySQL  
2️⃣ Execute `schema.sql` in MySQL to create database + tables  
3️⃣ Install dependencies:

```bash
pip install -r requirements.txt

4️⃣ Run the program:
python main.py
👉 Login with:
Username: admin
Password: admin123
