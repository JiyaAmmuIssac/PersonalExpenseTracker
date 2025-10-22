
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import db_manager

CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Entertainment", "Others"]

def open_add_window(parent):
    win = tk.Toplevel(parent)
    win.title("Add Expense")
    win.geometry("360x280")

    tk.Label(win, text="Date (YYYY-MM-DD)").pack(pady=4)
    date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
    tk.Entry(win, textvariable=date_var).pack()

    tk.Label(win, text="Category").pack(pady=4)
    category_var = tk.StringVar(value=CATEGORIES[0])
    ttk.Combobox(win, textvariable=category_var, values=CATEGORIES, state='readonly').pack()

    tk.Label(win, text="Amount").pack(pady=4)
    amount_var = tk.StringVar()
    tk.Entry(win, textvariable=amount_var).pack()

    tk.Label(win, text="Note").pack(pady=4)
    note_var = tk.StringVar()
    tk.Entry(win, textvariable=note_var).pack()

    def save():
        date = date_var.get().strip()
        category = category_var.get().strip()
        amount = amount_var.get().strip()
        note = note_var.get().strip()
        if not date or not category or not amount:
            messagebox.showerror("Validation", "Date, Category and Amount are required.")
            return
        try:
            amt = float(amount)
        except ValueError:
            messagebox.showerror("Validation", "Amount must be numeric.")
            return
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Validation", "Date must be YYYY-MM-DD")
            return
        db_manager.add_expense(date, category, amt, note)
        messagebox.showinfo("Saved", "Expense saved successfully.")
        win.destroy()

    tk.Button(win, text="Save", command=save).pack(pady=8)
    tk.Button(win, text="Cancel", command=win.destroy).pack()
