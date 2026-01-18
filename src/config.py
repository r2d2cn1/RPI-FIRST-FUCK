from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()  # like import.meta.env

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
    DB_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
    DB_NAME = os.getenv("POSTGRES_DB", "hil_test")
    DB_USER = os.getenv("POSTGRES_USER", "postgres")
    DB_PASS = os.getenv("POSTGRES_PASSWORD")

    LOG_LEVEL = "INFO"