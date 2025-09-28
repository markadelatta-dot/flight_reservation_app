import sqlite3

DB_NAME = "flights.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def setup_database():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        flight_number TEXT,
        departure TEXT,
        destination TEXT,
        date TEXT,
        seat_number TEXT
    )""")
    conn.commit()
    conn.close()
