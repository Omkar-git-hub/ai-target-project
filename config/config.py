"""
Configuration module for the project.
"""
import os
from enum import Enum

class Environment(Enum):
    """Environment types."""
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'
    TESTING = 'testing'

class Config:
    """Base configuration class."""
    DEBUG = False
    TESTING = False
    ENV = Environment.PRODUCTION

class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True
    ENV = Environment.DEVELOPMENT

class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    ENV = Environment.TESTING

class ProductionConfig(Config):
    """Production configuration class."""
    ENV = Environment.PRODUCTION

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config(env):
    """Get configuration based on environment."""
    return config.get(env, config['default'])()