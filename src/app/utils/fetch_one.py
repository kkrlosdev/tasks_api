def fetch_one(cursor) -> dict | None:
    columns = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()

    if row is None:
        return None

    return {col: val for col, val in zip(columns, row)}
