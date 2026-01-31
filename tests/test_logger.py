from jirakpipybuddy.logger import get_logger

def test_logger_is_initializing():
    logger = get_logger()
    assert logger is not None