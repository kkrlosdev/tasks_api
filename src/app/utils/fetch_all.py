from datetime import datetime, date
from decimal import Decimal
from sqlite3.dbapi2 import Cursor
from typing import Any

def fetch_all(cursor: Cursor) -> list[dict[str, Any]]:
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    
    def serialize(value: Any):
        if isinstance(value, (datetime, date)):
            return value.strftime('%Y-%m-%d')
        if isinstance(value, Decimal):
            return float(value)
        if isinstance(value, str):
            return value.strip()
        return value

    return [
        {col: serialize(val) for col, val in zip(columns, row)}
        for row in rows
    ]