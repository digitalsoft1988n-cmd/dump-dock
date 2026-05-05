import argparse
from storage.r2_client import R2Client
from core.utils import get_latest_key
from core.config import config
from services.backup_service import create_backup
from services.restore_service import restore_backup


def main():
    parser = argparse.ArgumentParser(prog="dump-dock")
    subparsers = parser.add_subparsers(dest="command")

    # backup
    subparsers.add_parser("backup")

    # list
    subparsers.add_parser("list")

    # latest
    subparsers.add_parser("latest")

    # restore
    restore_parser = subparsers.add_parser("restore")
    restore_parser.add_argument("--file", help="Specific backup key")
    restore_parser.add_argument(
        "--latest", action="store_true", help="Restore latest backup"
    )

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--file", required=True, help="Backup key to delete")

    args = parser.parse_args()
    r2 = R2Client(config)

    if args.command == "backup":
        print("Creating backup...")
        filepath = create_backup(config)
        key = r2.upload_file(filepath)
        print(f"Uploaded: {key}")

    elif args.command == "list":
        files = r2.list_files()
        for f in files:
            print(f)

    elif args.command == "latest":
        files = r2.list_files()
        latest = get_latest_key(files)

        if latest:
            print(latest)
        else:
            print("No backups found")

    elif args.command == "restore":
        if args.latest:
            files = r2.list_files()
            key = get_latest_key(files)

            if not key:
                print("No backups found")
                return

        elif args.file:
            key = args.file

        else:
            print("Provide --file or --latest")
            return

        print(f"Downloading {key}...")
        filepath = r2.download_file(key)

        print("Restoring...")
        restore_backup(config, filepath)

        print("Restore complete")

    elif args.command == "delete":
        r2.delete_file(args.file)
        print(f"Deleted: {args.file}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
