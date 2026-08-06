"""
Pytest configuration.
"""
import pytest
from config import config

@pytest.fixture
def config():
    """Get configuration."""
    return config.get('testing')()