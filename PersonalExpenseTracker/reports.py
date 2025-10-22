
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
import db_manager

def open_report_window(parent):
    win = tk.Toplevel(parent)
    win.title("Reports")
    win.geometry("400x200")

    tk.Label(win, text="Reports - Monthly Summary").pack(pady=6)

    def show_pie():
        month_prefix = datetime.now().strftime('%Y-%m')
        data = db_manager.get_monthly_summary(month_prefix)
        if not data:
            messagebox.showinfo("No Data", "No records found for this month.")
            return
        categories = [r[0] for r in data]
        amounts = [r[1] for r in data]
        plt.figure(figsize=(6,6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title(f"Spending for {month_prefix}")
        plt.show()

    tk.Button(win, text="Show Current Month Pie", command=show_pie).pack(pady=6)
    tk.Button(win, text="Close", command=win.destroy).pack()
