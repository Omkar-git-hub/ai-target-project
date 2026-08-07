from package.utils import get_app_name, get_app_version

def test_get_app_name():
    assert get_app_name() == "ai-target-project"

def test_get_app_version():
    assert get_app_version() == "1.0.0"