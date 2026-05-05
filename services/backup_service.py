import subprocess
import os
from datetime import datetime


def create_backup(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{config.SRC_DB_NAME}-{timestamp}.dump"
    filepath = os.path.join("backups", filename)

    os.makedirs("backups", exist_ok=True)

    env = os.environ.copy()
    env["PGPASSWORD"] = config.SRC_DB_PASSWORD

    command = [
        "pg_dump",
        "-h",
        config.SRC_DB_HOST,
        "-p",
        str(config.SRC_DB_PORT),
        "-U",
        config.SRC_DB_USER,
        "-d",
        config.SRC_DB_NAME,
        "-F",
        "c",
        "-f",
        filepath,
    ]

    result = subprocess.run(command, env=env)

    if result.returncode != 0:
        raise Exception("Backup failed")

    return filepath
