from typing import Dict

class Config:
    def __init__(self, env: str):
        self.env = env
        self.configs = {
            'dev': {
                'database_url': 'sqlite:///dev.db',
                'debug': True
            },
            'prod': {
                'database_url': 'postgresql://user:password@host:port/dbname',
                'debug': False
            }
        }

    def get_config(self) -> Dict:
        return self.configs.get(self.env)