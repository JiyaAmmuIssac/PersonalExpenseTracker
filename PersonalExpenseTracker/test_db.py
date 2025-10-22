
import os
import db_manager

TEST_DB = 'test_expense.db'

def setup_module(module):
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    db_manager.init_db(TEST_DB)

def teardown_module(module):
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_add_and_get():
    db_manager.add_expense('2025-10-22', 'Food', 150.0, 'Lunch', db_file=TEST_DB)
    rows = db_manager.get_all_expenses(db_file=TEST_DB)
    assert len(rows) == 1
    assert rows[0][2] == 'Food'
