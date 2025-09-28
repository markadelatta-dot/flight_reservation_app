import tkinter as tk
from tkinter import ttk, messagebox
import database
import booking
import edit_reservation

def reservations_page(root):
    frame = tk.Frame(root)

    tree = ttk.Treeview(frame, columns=("id","name","flight","dep","dest","date","seat"), show="headings")
    for col in ("id","name","flight","dep","dest","date","seat"):
        tree.heading(col, text=col.capitalize())
    tree.pack(fill="both", expand=True)

    def refresh_tree():
        for row in tree.get_children():
            tree.delete(row)
        conn = database.connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM reservations")
        rows = c.fetchall()
        conn.close()
        for r in rows:
            tree.insert("", "end", values=r)

    def delete_selected():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation")
            return
        res_id = tree.item(selected[0])["values"][0]
        conn = database.connect_db()
        c = conn.cursor()
        c.execute("DELETE FROM reservations WHERE id=?", (res_id,))
        conn.commit()
        conn.close()
        refresh_tree()

    btns = tk.Frame(frame)
    btns.pack(pady=5)

    tk.Button(btns, text="Book Flight", command=lambda: booking.booking_form(root, tree, refresh_tree)).grid(row=0, column=0, padx=5)
    tk.Button(btns, text="Edit", command=lambda: edit_reservation.edit_form(root, tree.item(tree.selection()[0])["values"] if tree.selection() else None, refresh_tree)).grid(row=0, column=1, padx=5)
    tk.Button(btns, text="Delete", command=delete_selected).grid(row=0, column=2, padx=5)

    refresh_tree()
    return frame
