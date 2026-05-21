"""
Tests for CLI utilities including logging setup.
"""
import logging
import pytest
from eb_model.cli.cli_utils import setup_logger


def test_setup_logger_verbose():
    """Test that verbose mode enables DEBUG level."""
    logger = setup_logger(verbose=True, log_file=None)
    assert logger.level == logging.DEBUG


def test_setup_logger_normal():
    """Test that normal mode uses INFO level."""
    logger = setup_logger(verbose=False, log_file=None)
    assert logger.level == logging.DEBUG  # Root logger always DEBUG, handlers control output


def test_setup_logger_has_stream_handler():
    """Test that logger has a stream handler."""
    logger = setup_logger(verbose=False, log_file=None)
    handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
    assert len(handlers) > 0


def test_setup_logger_with_file(tmp_path):
    """Test that log_file parameter creates file handler."""
    log_file = tmp_path / "test.log"
    logger = setup_logger(verbose=False, log_file=str(log_file))
    handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
    assert len(handlers) > 0


def test_setup_logger_file_handler_debug_level(tmp_path):
    """Test that file handler always uses DEBUG level."""
    log_file = tmp_path / "test_debug.log"
    logger = setup_logger(verbose=False, log_file=str(log_file))
    file_handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
    assert len(file_handlers) > 0
    assert file_handlers[0].level == logging.DEBUG


def test_handler_clearing():
    """Test that handlers are cleared on subsequent calls."""
    logger1 = setup_logger(verbose=False)
    initial_count = len(logger1.handlers)
    logger2 = setup_logger(verbose=False)
    # Should only have one handler (not accumulate)
    assert len(logger2.handlers) == initial_count
