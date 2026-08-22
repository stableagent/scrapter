from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
DATABASE_DIR = DATA_DIR / "database"
IMAGE_DIR = DATA_DIR / "images"
EXPORT_DIR = DATA_DIR / "exports"
CACHE_DIR = DATA_DIR / "cache"
STATE_DIR = DATA_DIR / "state"
LOG_DIR = BASE_DIR / "logs"

APP_NAME = "Premium Handpiece Parts Scraper"
BASE_URL = "https://premiumhandpieceparts.com"
