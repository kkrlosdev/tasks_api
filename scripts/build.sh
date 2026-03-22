#!/usr/bin/env bash
set -e

MODE=$1
OPTION=$2

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

COMPOSE_FILE="$PROJECT_ROOT/docker/docker-compose.yml"
ENV_FILE="$PROJECT_ROOT/.env"

# --- Validación de modo ---
if [ -z "$MODE" ]; then
  echo "Usage: ./scripts/build.sh [up|down] [--no-build]"
  exit 1
fi

# --- Validación de opción ---
if [ -n "$OPTION" ] && [ "$OPTION" != "--no-build" ]; then
  echo "Unknown option: $OPTION"
  exit 1
fi

# --- DOWN ---
if [ "$MODE" = "down" ]; then
  echo "Stopping services..."
  docker compose --env-file "$ENV_FILE" -f "$COMPOSE_FILE" down
  exit 0
fi

# --- UP ---
if [ "$MODE" = "up" ]; then
  echo "Starting services..."

  if [ "$OPTION" = "--no-build" ]; then
    docker compose \
      --env-file "$ENV_FILE" \
      -f "$COMPOSE_FILE" \
      up -d
  else
    docker compose \
      --env-file "$ENV_FILE" \
      -f "$COMPOSE_FILE" \
      up --build -d
  fi

  exit 0
fi

# --- UNKNOWN ---
echo "[!] Unknown mode: $MODE"
echo "Usage: ./scripts/build.sh [up|down] [--no-build]"
exit 1