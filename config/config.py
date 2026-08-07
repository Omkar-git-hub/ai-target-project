"""
Configuration module for the project.

This module contains all configuration-related settings and constants.
"""

import os

class Config:
    """
    Base configuration class.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')

class DevelopmentConfig(Config):
    """
    Development configuration class.
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configuration class.
    """
    TESTING = True

class ProductionConfig(Config):
    """
    Production configuration class.
    """
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}