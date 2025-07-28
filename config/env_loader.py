from pathlib import Path
from dotenv import load_dotenv


def load_env():
    project_dir = Path(__file__).resolve().parents[1]
    load_dotenv(project_dir / ".env", override=True)

