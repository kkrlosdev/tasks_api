import sqlite3

def connect(db_name: str = "db.db"):
    try:
        conn = sqlite3.connect(db_name, timeout=10)
        return conn
    except Exception as e:
        raise Exception(f"Could not connect to database: {e}")