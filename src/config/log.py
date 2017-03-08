"""
Logging
"""
import logging
import logging.config

from src.config import LOGGING_FILE


def init():
    """
    Initialize logging.
    """
    logging.config.fileConfig(LOGGING_FILE)
