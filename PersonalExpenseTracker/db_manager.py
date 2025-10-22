
import sqlite3
from typing import List, Tuple, Optional

DB_FILE = "expense.db"

CREATE_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    note TEXT
);
'''

def get_connection(db_file: str = DB_FILE):
    conn = sqlite3.connect(db_file)
    return conn

def init_db(db_file: str = DB_FILE):
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute(CREATE_TABLE_SQL)
    conn.commit()
    conn.close()

def add_expense(date: str, category: str, amount: float, note: Optional[str] = None, db_file: str = DB_FILE) -> int:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
                (date, category, amount, note))
    conn.commit()
    rowid = cur.lastrowid
    conn.close()
    return rowid

def get_all_expenses(db_file: str = DB_FILE) -> List[Tuple]:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT id, date, category, amount, note FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id: int, db_file: str = DB_FILE) -> None:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def update_expense(expense_id: int, date: str, category: str, amount: float, note: Optional[str] = None, db_file: str = DB_FILE) -> None:
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("UPDATE expenses SET date = ?, category = ?, amount = ?, note = ? WHERE id = ?",
                (date, category, amount, note, expense_id))
    conn.commit()
    conn.close()

def get_monthly_summary(month_prefix: str, db_file: str = DB_FILE):
    conn = get_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM expenses WHERE date LIKE ? GROUP BY category", (month_prefix + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows
