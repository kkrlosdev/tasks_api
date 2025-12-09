import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.db")    

def connect():
    try:
        conn = sqlite3.connect(DB_PATH, timeout=10)
        return conn
    except Exception as e:
        raise Exception(f"Could not connect to database: {e}")