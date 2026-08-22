from loguru import logger

from config.settings import LOG_DIR

LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(LOG_DIR / "crawler.log", rotation="10 MB", retention="30 days", level="INFO")
logger.add(LOG_DIR / "error.log", rotation="10 MB", retention="30 days", level="ERROR")
