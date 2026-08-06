"""
Configure the project.
"""
import os
from config import config

def configure():
    """Configure the project."""
    env = os.environ.get('ENV', 'development')
    return config.get(env, config['default'])()