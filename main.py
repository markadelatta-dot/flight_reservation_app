import tkinter as tk
import database
import reservations

def main():
    database.setup_database()

    root = tk.Tk()
    root.title("Flight Reservation App")
    root.geometry("800x500")

    page = reservations.reservations_page(root)
    page.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
