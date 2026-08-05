import os

class Config:
    def __init__(self):
        self.debug = os.environ.get("DEBUG", False)