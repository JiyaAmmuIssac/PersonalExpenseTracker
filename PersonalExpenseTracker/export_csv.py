
import csv
import db_manager

def export_all_csv(filename: str = "expenses_export.csv"):
    rows = db_manager.get_all_expenses()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "date", "category", "amount", "note"])
        writer.writerows(rows)
    print(f"Exported {len(rows)} records to {filename}")
