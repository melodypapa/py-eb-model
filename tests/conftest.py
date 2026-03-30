"""
Pytest configuration for eb_model tests.

This module provides fixtures for test setup and teardown.
"""
import pytest


@pytest.fixture(autouse=True, scope="function")
def reset_ebmodel_singleton():
    """Reset EBModel singleton before each test."""
    from eb_model.models.core.eb_doc import EBModel
    EBModel._EBModel__instance = None
    yield
