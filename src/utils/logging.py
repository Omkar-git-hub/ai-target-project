"""
Logging utilities.
"""
import logging
from config import enums

def get_logger(name):
    """Get a logger."""
    logger = logging.getLogger(name)
    logger.setLevel(enums.LogLevel.INFO.value)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger