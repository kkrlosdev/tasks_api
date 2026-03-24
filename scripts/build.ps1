#!/usr/bin/env pwsh

$ErrorActionPreference = "Stop"

$MODE = $args[0]
$OPTION = $args[1]

# Obtener rutas
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$PROJECT_ROOT = Split-Path -Parent $SCRIPT_DIR

$COMPOSE_FILE = Join-Path $PROJECT_ROOT "docker/docker-compose.yml"
$ENV_FILE = Join-Path $PROJECT_ROOT ".env"

# --- Validación de modo ---
if (-not $MODE) {
    Write-Output "Usage: ./scripts/build.ps1 [up|down] [--no-build]"
    exit 1
}

# --- Validación de opción ---
if ($OPTION -and $OPTION -ne "--no-build") {
    Write-Output "Unknown option: $OPTION"
    exit 1
}

# --- DOWN ---
if ($MODE -eq "down") {
    Write-Output "Stopping services..."
    docker compose --env-file "$ENV_FILE" -f "$COMPOSE_FILE" down
    exit 0
}

# --- UP ---
if ($MODE -eq "up") {
    Write-Output "Starting services..."

    if ($OPTION -eq "--no-build") {
        docker compose `
            --env-file "$ENV_FILE" `
            -f "$COMPOSE_FILE" `
            up -d
    }
    else {
        docker compose `
            --env-file "$ENV_FILE" `
            -f "$COMPOSE_FILE" `
            up --build -d
    }

    exit 0
}

# --- UNKNOWN ---
Write-Output "[!] Unknown mode: $MODE"
Write-Output "Usage: ./scripts/build.ps1 [up|down] [--no-build]"
exit 1