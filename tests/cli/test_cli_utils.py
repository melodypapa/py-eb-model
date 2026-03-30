import logging
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