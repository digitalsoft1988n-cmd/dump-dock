import subprocess
import os


def restore_backup(config, filepath):
    env = os.environ.copy()
    env["PGPASSWORD"] = config.LOCAL_DB_PASSWORD

    command = [
        "pg_restore",
        "-h", config.LOCAL_DB_HOST,
        "-p", str(config.LOCAL_DB_PORT),
        "-U", config.LOCAL_DB_USER,
        "-d", config.LOCAL_DB_NAME,
        "--clean",
        "--if-exists",
        "--no-owner",
        "--role", config.LOCAL_DB_USER,
        filepath
    ]

    result = subprocess.run(command, env=env)

    if result.returncode != 0:
        raise Exception("Restore failed")
