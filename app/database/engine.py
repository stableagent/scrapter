from sqlalchemy import create_engine

from config.settings import DATABASE_DIR

DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_URL = "sqlite:///data/database/products.db"
engine = create_engine(DATABASE_URL, future=True)
