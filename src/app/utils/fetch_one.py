from sqlite3.dbapi2 import Cursor
from typing import Any

def fetch_one(cursor: Cursor) -> dict[str, Any] | None:
    columns = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()

    if row is None:
        return None

    return {col: val for col, val in zip(columns, row)}
