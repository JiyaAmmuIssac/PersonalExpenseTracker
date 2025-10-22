
import tkinter as tk
from tkinter import ttk, messagebox
import db_manager

def open_view_window(parent):
    win = tk.Toplevel(parent)
    win.title("View Expenses")
    win.geometry("640x360")

    cols = ("id", "date", "category", "amount", "note")
    tree = ttk.Treeview(win, columns=cols, show='headings')
    for c in cols:
        tree.heading(c, text=c.capitalize())
        tree.column(c, width=100)
    tree.pack(fill='both', expand=True)

    def load_data():
        for r in tree.get_children():
            tree.delete(r)
        rows = db_manager.get_all_expenses()
        for row in rows:
            tree.insert('', 'end', values=row)

    def delete_selected():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select", "Select a record to delete")
            return
        item = tree.item(sel[0])
        eid = item['values'][0]
        if messagebox.askyesno("Confirm", "Delete selected record?"):
            db_manager.delete_expense(eid)
            load_data()

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=6)
    tk.Button(btn_frame, text="Refresh", command=load_data).pack(side='left', padx=6)
    tk.Button(btn_frame, text="Delete", command=delete_selected).pack(side='left', padx=6)

    load_data()
