# ============================================================
# EVENT REGISTRATION SYSTEM
# Python + Tkinter + ttkbootstrap + MySQL
# ============================================================

import mysql.connector
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, END, ttk

# ------------------ DATABASE CONFIG ------------------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',              # your MySQL username
    'password': 'RAHUL123', # your MySQL password
    'database': 'event_system'
}

# ------------------ DATABASE CONNECTION ------------------
def connect_db():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
        return None

# ============================================================
#                       MAIN APPLICATION
# ============================================================
class EventRegistrationApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Event Registration System")
        self.root.geometry("900x550")

        # Title Label
        tb.Label(root, text="EVENT REGISTRATION SYSTEM", font=("Arial", 22, "bold")).pack(pady=15)

        self.create_form()
        self.create_table()
        self.load_data()

    # --------------------------------------------------------
    #                     INPUT FORM
    # --------------------------------------------------------
    def create_form(self):
        frame = tb.Frame(self.root)
        frame.pack(pady=10)

        # Input fields
        tb.Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tb.Entry(frame, width=30)
        self.name_entry.grid(row=0, column=1)

        tb.Label(frame, text="Email:").grid(row=1, column=0, padx=10, pady=5)
        self.email_entry = tb.Entry(frame, width=30)
        self.email_entry.grid(row=1, column=1)

        tb.Label(frame, text="Phone:").grid(row=2, column=0, padx=10, pady=5)
        self.phone_entry = tb.Entry(frame, width=30)
        self.phone_entry.grid(row=2, column=1)

        tb.Label(frame, text="Event Name:").grid(row=3, column=0, padx=10, pady=5)
        self.event_entry = tb.Entry(frame, width=30)
        self.event_entry.grid(row=3, column=1)

        # Buttons
        btn_frame = tb.Frame(self.root)
        btn_frame.pack(pady=10)

        tb.Button(btn_frame, text="Register", bootstyle=SUCCESS, width=15, command=self.add_participant).grid(row=0, column=0, padx=10)
        tb.Button(btn_frame, text="Update", bootstyle=INFO, width=15, command=self.update_participant).grid(row=0, column=1, padx=10)
        tb.Button(btn_frame, text="Delete", bootstyle=DANGER, width=15, command=self.delete_participant).grid(row=0, column=2, padx=10)
        tb.Button(btn_frame, text="Clear", bootstyle=SECONDARY, width=15, command=self.clear_form).grid(row=0, column=3, padx=10)

    # --------------------------------------------------------
    #                     TABLE VIEW
    # --------------------------------------------------------
    def create_table(self):
        columns = ("ID","Name","Email","Phone","Event","Date")

        self.table = ttk.Treeview(self.root, columns=columns, show="headings", height=12)
        self.table.pack(pady=10)

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=120)

        self.table.bind("<<TreeviewSelect>>", self.on_row_select)

    # --------------------------------------------------------
    #                    LOAD DATA
    # --------------------------------------------------------
    def load_data(self):
        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()
        cursor.execute("SELECT * FROM participants")
        rows = cursor.fetchall()

        self.table.delete(*self.table.get_children())

        for row in rows:
            self.table.insert("", END, values=row)

        db.close()

    # --------------------------------------------------------
    #                    ADD PARTICIPANT
    # --------------------------------------------------------
    def add_participant(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        event = self.event_entry.get()

        if not(name and email and phone and event):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        db = connect_db()
        cursor = db.cursor()

        query = "INSERT INTO participants (name,email,phone,event_name) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (name, email, phone, event))
        db.commit()
        db.close()

        messagebox.showinfo("Success", "Registration Successful!")
        self.load_data()
        self.clear_form()

    # --------------------------------------------------------
    #                 SELECT ROW FROM TABLE
    # --------------------------------------------------------
    def on_row_select(self, event):
        selected = self.table.focus()
        values = self.table.item(selected, 'values')

        if values:
            self.selected_id = values[0]
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, values[1])

            self.email_entry.delete(0, END)
            self.email_entry.insert(0, values[2])

            self.phone_entry.delete(0, END)
            self.phone_entry.insert(0, values[3])

            self.event_entry.delete(0, END)
            self.event_entry.insert(0, values[4])

    # --------------------------------------------------------
    #                 UPDATE PARTICIPANT
    # --------------------------------------------------------
    def update_participant(self):
        if not hasattr(self, "selected_id"):
            messagebox.showwarning("Warning", "Select a record to update.")
            return

        db = connect_db()
        cursor = db.cursor()

        query = """UPDATE participants 
                   SET name=%s, email=%s, phone=%s, event_name=%s 
                   WHERE id=%s"""

        cursor.execute(query, (
            self.name_entry.get(),
            self.email_entry.get(),
            self.phone_entry.get(),
            self.event_entry.get(),
            self.selected_id
        ))

        db.commit()
        db.close()

        messagebox.showinfo("Success", "Record Updated!")
        self.load_data()
        self.clear_form()

    # --------------------------------------------------------
    #                 DELETE PARTICIPANT
    # --------------------------------------------------------
    def delete_participant(self):
        if not hasattr(self, "selected_id"):
            messagebox.showwarning("Warning", "Select a record to delete.")
            return

        db = connect_db()
        cursor = db.cursor()

        cursor.execute("DELETE FROM participants WHERE id=%s", (self.selected_id,))
        db.commit()
        db.close()

        messagebox.showinfo("Deleted", "Participant removed.")
        self.load_data()
        self.clear_form()

    # --------------------------------------------------------
    #                    CLEAR FORM
    # --------------------------------------------------------
    def clear_form(self):
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.event_entry.delete(0, END)
        self.selected_id = None


# ============================================================
#                      RUN APPLICATION
# ============================================================
if __name__ == "__main__":
    app = tb.Window(themename="minty")
    EventRegistrationApp(app)
    app.mainloop()
