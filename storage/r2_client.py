import boto3
import os


class R2Client:
    def __init__(self, config):
        self.bucket = config.R2_BUCKET_NAME

        self.client = boto3.client(
            "s3",
            endpoint_url=config.R2_ENDPOINT,
            aws_access_key_id=config.R2_ACCESS_KEY,
            aws_secret_access_key=config.R2_SECRET_KEY,
            region_name="auto",
        )

    def upload_file(self, file_path, key=None):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} not found")

        if key is None:
            key = f"backups/{os.path.basename(file_path)}"

        self.client.upload_file(file_path, self.bucket, key)

        return key

    def download_file(self, key, download_dir="downloads"):
        os.makedirs(download_dir, exist_ok=True)

        local_path = os.path.join(download_dir, os.path.basename(key))

        self.client.download_file(self.bucket, key, local_path)

        return local_path

    def list_files(self, prefix="backups/"):
        response = self.client.list_objects_v2(Bucket=self.bucket, Prefix=prefix)

        return [obj["Key"] for obj in response.get("Contents", [])]

    def delete_file(self, key):
        self.client.delete_object(Bucket=self.bucket, Key=key)
