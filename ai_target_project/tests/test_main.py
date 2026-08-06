import pytest
from ai_target_project.main import add_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3