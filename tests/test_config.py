from ai_target_project.config import config

def test_config():
    assert config['development'].DEBUG
    assert not config['production'].DEBUG