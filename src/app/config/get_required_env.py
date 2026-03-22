import os

def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise EnvironmentError(f"Variable de entorno '{name}' no definida. Revisar o crear archivo .env")
    return value