import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.config import settings


def setup_logging() -> logging.Logger:
    """Configure application logging."""
    log_path = Path(settings.log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # TODO: implement.
    # Note: The log directory creation logic is already
    # implemented above, you don't have to care about it.
    # Just implement the logging configuration directly below.

    root = logging.getLogger()
    if root.handlers:
        return root

    formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler = RotatingFileHandler(
    settings.log_file,
    maxBytes=settings.log_max_bytes,
    backupCount=settings.log_backup_count,
)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    root.setLevel(settings.log_level)
    root.addHandler(file_handler)
    root.addHandler(stream_handler)

    return root