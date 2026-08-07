"""
Enum module for configuration.
"""
from enum import Enum

class Environment(Enum):
    """
    Environment enum.
    """
    DEVELOPMENT = 'development'
    TESTING = 'testing'
    PRODUCTION = 'production'