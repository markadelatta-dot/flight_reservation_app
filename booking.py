import tkinter as tk
from tkinter import messagebox
import database

def booking_form(root, tree, refresh_tree):
    win = tk.Toplevel(root)
    win.title("Book Flight")

    labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat #"]
    entries = {}

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, pady=5, padx=5)
        e = tk.Entry(win)
        e.grid(row=i, column=1, pady=5, padx=5)
        entries[text] = e

    def add_reservation():
        data = [entries[l].get() for l in labels]
        if "" in data[:5]:  # check first 5 fields
            messagebox.showwarning("Warning", "Please fill in all fields")
            return
        conn = database.connect_db()
        c = conn.cursor()
        c.execute("INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number) VALUES (?, ?, ?, ?, ?, ?)", data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Saved", "Reservation added!")
        refresh_tree()
        win.destroy()

    tk.Button(win, text="Submit", command=add_reservation).grid(row=len(labels), column=0, columnspan=2, pady=10)
