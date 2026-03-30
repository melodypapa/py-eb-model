"""
CLI Utilities.

Shared utilities for CLI operations including logging setup.
"""
import sys
import os
import logging
from typing import Optional


def setup_logger(verbose: bool = False, log_file: Optional[str] = None) -> logging.Logger:
    """
    Set up logging configuration for CLI.

    Args:
        verbose: Enable DEBUG level output
        log_file: Optional path to log file. If None, no file logging.

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    # Clear existing handlers
    logger.handlers.clear()

    # Set up stdout handler
    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    if verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    stdout_handler.setLevel(log_level)
    logger.addHandler(stdout_handler)

    # Set up file handler if specified
    if log_file:
        if os.path.exists(log_file):
            os.remove(log_file)

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

    # Set root logger level to DEBUG (handlers control actual output)
    logger.setLevel(logging.DEBUG)

    return logger