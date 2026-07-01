from datetime import datetime

from app.config.get_required_env import get_required_env

SERVICE_NAME = get_required_env("SERVICE_NAME")
ENVIRONMENT = get_required_env("ENVIRONMENT")
STARTUP_TIME = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
API_PORT = get_required_env("API_PORT")
BUILD_TIME = get_required_env("BUILD_TIME")
