"""
Enums for the project configuration.
"""
from enum import Enum

class LogLevel(Enum):
    """Log levels."""
    DEBUG = 'debug'
    INFO = 'info'
    WARNING = 'warning'
    ERROR = 'error'
    CRITICAL = 'critical'