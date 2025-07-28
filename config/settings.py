import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"
DATASETS_PATH = PROJECT_ROOT / "datasets/"


load_dotenv(dotenv_path=ENV_PATH, override=True)
CF_ACCOUNT_ID = os.getenv("CF_ACCOUNT_ID")
CF_ACCESS_KEY_ID = os.getenv("CF_ACCESS_KEY_ID")
CF_SECRET_ACCESS_KEY = os.getenv("CF_SECRET_ACCESS_KEY")
CF_BUCKET_NAME = os.getenv("CF_BUCKET_NAME")