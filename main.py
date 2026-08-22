from loguru import logger

from config import logging as _logging  # noqa: F401
from config.settings import APP_NAME


if __name__ == "__main__":
    logger.info(f"{APP_NAME} started successfully.")
