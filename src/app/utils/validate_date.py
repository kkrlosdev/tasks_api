from datetime import datetime

def validate_date(value: str) -> bool:
    if not value or not isinstance(value, str):
        return False

    formats = [
        "%d-%m-%Y",
        "%d-%m-%Y %H:%M:%S"
    ]

    for format in formats:
        try:
            datetime.strptime(value, format)
            return True
        except ValueError:
            continue

    return False