from jirakpipybuddy.config import get_config, AppConfig


def test_get_config_returning_not_none():
    config = get_config()
    assert config is not None


def test_get_config_returning_right_class():
    config = get_config()
    assert isinstance(config, AppConfig)


