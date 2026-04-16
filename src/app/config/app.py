import datetime

from app.config.get_required_env import get_required_env

SERVICE_NAME = get_required_env("SERVICE_NAME")
ENVIRONMENT = get_required_env("ENVIRONMENT")
STARTUP_TIME = datetime.datetime.now(datetime.UTC).isoformat()
API_PORT = get_required_env("API_PORT")
BUILD_TIME = get_required_env("BUILD_TIME") or STARTUP_TIME