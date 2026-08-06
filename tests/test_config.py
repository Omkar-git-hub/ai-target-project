import pytest
from src.config import Config

def test_config():
    config = Config()
    assert config is not None