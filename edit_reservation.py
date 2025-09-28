import tkinter as tk
from tkinter import messagebox
import database

def edit_form(root, selected, refresh_tree):
    if not selected:
        messagebox.showwarning("Warning", "Please select a reservation")
        return

    res_id, name, flight, dep, dest, date, seat = selected

    win = tk.Toplevel(root)
    win.title("Edit Reservation")

    labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat #"]
    entries = {}

    values = [name, flight, dep, dest, date, seat]

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, pady=5, padx=5)
        e = tk.Entry(win)
        e.insert(0, values[i])
        e.grid(row=i, column=1, pady=5, padx=5)
        entries[text] = e

    def update_reservation():
        data = [entries[l].get() for l in labels]
        if "" in data[:5]:
            messagebox.showwarning("Warning", "Please fill in all fields")
            return
        conn = database.connect_db()
        c = conn.cursor()
        c.execute("""UPDATE reservations SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=? WHERE id=?""",
                  (*data, res_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Updated", "Reservation updated!")
        refresh_tree()
        win.destroy()

    tk.Button(win, text="Update", command=update_reservation).grid(row=len(labels), column=0, columnspan=2, pady=10)
