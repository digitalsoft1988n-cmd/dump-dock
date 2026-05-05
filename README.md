# Dump Dock

A lightweight Python utility to automate PostgreSQL backups using `pg_dump`, upload them to Cloudflare R2 object storage, and restore them to a local database when needed.

---

## Features

* Dump remote/server PostgreSQL databases using `pg_dump`
* Upload backups directly to Cloudflare R2
* Restore backups to a local PostgreSQL instance
* Simple CLI interface
* Minimal configuration
* Suitable for cron jobs and automation workflows

---

## Installation

```bash
git clone https://github.com/your-username/dump-dock.git
cd dump-dock
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file or export environment variables:

```env
# =========================
# Server (Source) Database
# =========================
SRC_DB_HOST=your_server_host
SRC_DB_PORT=5432
SRC_DB_NAME=your_database
SRC_DB_USER=your_username
SRC_DB_PASSWORD=your_password

# =========================
# Local (Destination) Database
# =========================
LOCAL_DB_HOST=localhost
LOCAL_DB_PORT=5432
LOCAL_DB_NAME=your_local_db
LOCAL_DB_USER=your_local_user
LOCAL_DB_PASSWORD=your_local_password

# =========================
# Cloudflare R2
# =========================
R2_ACCESS_KEY=your_access_key
R2_SECRET_KEY=your_secret_key
R2_BUCKET_NAME=your_bucket
R2_ENDPOINT=https://<account_id>.r2.cloudflarestorage.com
```

---

## Usage

### Backup and Upload

```bash
python main.py backup
```

* Connects to the source (server) database
* Creates a `.sql` dump using `pg_dump`
* Uploads the backup to the configured R2 bucket

---

### Restore to Local

```bash
python main.py restore <backup-file>
```

* Downloads the specified backup from R2
* Restores it into the local PostgreSQL database

---

## Project Structure

```
dump-dock/
│
├── main.py              # CLI entry point
├── backup.py            # Handles pg_dump operations
├── restore.py           # Handles restore operations
├── r2_client.py         # Cloudflare R2 interactions
├── config.py            # Environment/config handling
├── requirements.txt
└── README.md
```

---

## Example Workflow

1. Run backup:

   ```bash
   python main.py backup
   ```

2. File is uploaded to R2:

   ```
   backups/your_database-2026-05-05.sql
   ```

3. Restore when needed:

   ```bash
   python main.py restore backups/your_database-2026-05-05.sql
   ```

---

## Requirements

* Python 3.8+
* PostgreSQL client tools (`pg_dump`, `psql`)
* Cloudflare R2 credentials

---

## Security Notes

* Never commit `.env` files
* Use scoped R2 API keys with minimal permissions
* Consider encrypting backups before upload

---

## Future Improvements

* Incremental backups
* Compression support (gzip)
* Encryption (AES)
* Scheduled backups
* Multi-database support

---

## License

MIT License

---

## Contributing

Pull requests are welcome. For major changes, open an issue to discuss proposed changes first.

---
