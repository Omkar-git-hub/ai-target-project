"""
Application configuration.
"""

import os
from constants import *

class Config:
    def __init__(self):
        self.app_name = APP_NAME
        self.app_version = APP_VERSION
        self.api_base_url = API_BASE_URL
        self.api_timeout = API_TIMEOUT
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_username = DB_USERNAME
        self.db_password = DB_PASSWORD
        self.db_name = DB_NAME
        self.log_level = LOG_LEVEL
        self.log_format = LOG_FORMAT

    def get_config(self):
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "api_base_url": self.api_base_url,
            "api_timeout": self.api_timeout,
            "db_host": self.db_host,
            "db_port": self.db_port,
            "db_username": self.db_username,
            "db_password": self.db_password,
            "db_name": self.db_name,
            "log_level": self.log_level,
            "log_format": self.log_format
        }