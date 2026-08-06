"""
Application configuration.
"""

from constants import *

class Config:
    def __init__(self):
        self.app_name = APP_NAME
        self.app_version = APP_VERSION
        self.api_host = API_HOST
        self.api_port = API_PORT
        self.api_timeout = API_TIMEOUT
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_username = DB_USERNAME
        self.db_password = DB_PASSWORD
        self.db_name = DB_NAME
        self.log_level = LOG_LEVEL
        self.log_format = LOG_FORMAT