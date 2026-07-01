#!/usr/bin/env python
import argparse
from argparse import Namespace
from datetime import datetime
from pathlib import Path
import subprocess
import os

root_path = Path().absolute()

parser = argparse.ArgumentParser(prog="build")

subparsers = parser.add_subparsers(dest="action")

up = subparsers.add_parser("up")
up.add_argument("--no-build", action="store_true")
up.add_argument("--prod", action="store_true")

down = subparsers.add_parser("down")
down.add_argument("--prod", action="store_true")

args = parser.parse_args()


def detect_docker_folder():
    return (root_path / "docker").is_dir()


def build_command(args: Namespace) -> list[str]:
    docker_folder = detect_docker_folder()
    docker_folder = (root_path / "docker") if docker_folder is True else root_path
    command = [
        "docker",
        "compose",
        "--env-file",
        ".env",
        "-f",
    ]
    if args.prod is False:
        command.append(str(docker_folder / "docker-compose.yml"))
    else:
        command.append(str(docker_folder / "docker-compose-prod.yml"))

    if args.action == "up":
        command.append("up")
        if args.no_build is False:
            command.append("--build")
        command.append("-d")
    else:
        command.append("down")

    return command


command = build_command(args)

env = os.environ.copy()
env["BUILD_TIME"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

subprocess.run(command, check=True, env=env)
