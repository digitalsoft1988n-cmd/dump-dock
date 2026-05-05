import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        # Source DB (server)
        self.SRC_DB_HOST = os.getenv("SRC_DB_HOST")
        self.SRC_DB_PORT = int(os.getenv("SRC_DB_PORT", 5432))
        self.SRC_DB_NAME = os.getenv("SRC_DB_NAME")
        self.SRC_DB_USER = os.getenv("SRC_DB_USER")
        self.SRC_DB_PASSWORD = os.getenv("SRC_DB_PASSWORD")

        # Local DB
        self.LOCAL_DB_HOST = os.getenv("LOCAL_DB_HOST")
        self.LOCAL_DB_PORT = int(os.getenv("LOCAL_DB_PORT", 5432))
        self.LOCAL_DB_NAME = os.getenv("LOCAL_DB_NAME")
        self.LOCAL_DB_USER = os.getenv("LOCAL_DB_USER")
        self.LOCAL_DB_PASSWORD = os.getenv("LOCAL_DB_PASSWORD")

        # R2
        self.R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY")
        self.R2_SECRET_KEY = os.getenv("R2_SECRET_KEY")
        self.R2_BUCKET_NAME = os.getenv("R2_BUCKET_NAME")
        self.R2_ENDPOINT = os.getenv("R2_ENDPOINT")

    def validate(self):
        required = {
            "SRC_DB_HOST": self.SRC_DB_HOST,
            "SRC_DB_NAME": self.SRC_DB_NAME,
            "SRC_DB_USER": self.SRC_DB_USER,
            "SRC_DB_PASSWORD": self.SRC_DB_PASSWORD,
            "LOCAL_DB_HOST": self.LOCAL_DB_HOST,
            "LOCAL_DB_NAME": self.LOCAL_DB_NAME,
            "LOCAL_DB_USER": self.LOCAL_DB_USER,
            "LOCAL_DB_PASSWORD": self.LOCAL_DB_PASSWORD,
            "R2_ACCESS_KEY": self.R2_ACCESS_KEY,
            "R2_SECRET_KEY": self.R2_SECRET_KEY,
            "R2_BUCKET_NAME": self.R2_BUCKET_NAME,
            "R2_ENDPOINT": self.R2_ENDPOINT,
        }

        missing = [key for key, value in required.items() if not value]

        if missing:
            raise ValueError(f"Missing environment variables: {', '.join(missing)}")


# Initialize and validate immediately
config = Config()
config.validate()
