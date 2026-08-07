"""
Tests for the logging utility.
"""

import logging
from src.utils.logging import get_logger

def test_logger():
    logger = get_logger()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

    # Check if the log file exists
    with open('log.txt', 'r') as f:
        log_content = f.read()
        assert 'This is a debug message' in log_content
        assert 'This is an info message' in log_content
        assert 'This is a warning message' in log_content
        assert 'This is an error message' in log_content
        assert 'This is a critical message' in log_content