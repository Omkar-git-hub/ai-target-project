import pytest
from src.utils.helpers import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"