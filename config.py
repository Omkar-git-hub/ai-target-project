"""
Application configuration.
"""

import os
from constants import *

class Config:
    def __init__(self):
        self.app_name = APP_NAME
        self.version = VERSION
        self.api_url = API_URL
        self.api_key = API_KEY
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_username = DB_USERNAME
        self.db_password = DB_PASSWORD
        self.db_name = DB_NAME
        self.log_level = LOG_LEVEL
        self.log_file = LOG_FILE