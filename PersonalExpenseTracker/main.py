import tkinter as tk
from tkinter import ttk
from datetime import datetime
import db_manager
import add_expense
import view_expenses
import reports
import export_csv

# ------------------ App Setup ------------------
root = tk.Tk() # Create main window
root.title("My App")  # Set title
root.title("Personal Expense Tracker")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f0f4f8")  # light gray-blue background

# Use ttk style for modern look
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', font=('Helvetica', 12), padding=6, background="#4CAF50", foreground="white")
style.configure('TLabel', font=('Helvetica', 16, 'bold'), background="#f0f4f8", foreground="#333333")

# ------------------ Top Frame (Title) ------------------
top_frame = tk.Frame(root, bg="#f0f4f8")
top_frame.pack(pady=20)

title = tk.Label(top_frame, text=" Personal Expense Tracker ", font=("Helvetica", 20, "bold"), bg="#f0f4f8", fg="#1f2937")
title.pack()

# ------------------ Middle Frame (Buttons) ------------------
btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=30)

# Helper function to create buttons with hover effect
def create_button(text, command):
    btn = tk.Button(btn_frame, text=text, font=('Helvetica', 12), bg="#4CAF50", fg="white",
                    activebackground="#45a049", activeforeground="white", width=25, command=command)
    btn.pack(pady=6)
    return btn

# Button commands
db_manager.init_db()  # Ensure DB is initialized

create_button(" Add Expense", lambda: add_expense.open_add_window(root))
create_button(" View Expenses", lambda: view_expenses.open_view_window(root))
create_button(" View Reports", lambda: reports.open_report_window(root))
create_button(" Export to CSV", lambda: export_csv.export_all_csv())
create_button(" Exit", root.quit)

# ------------------ Footer ------------------
footer = tk.Label(root, text=f"Today: {datetime.now().strftime('%Y-%m-%d')}", font=("Helvetica", 10), bg="#f0f4f8", fg="#666666")
footer.pack(side='bottom', pady=10)

# ------------------ Run App ------------------
root.mainloop()
