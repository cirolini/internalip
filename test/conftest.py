import pytest

from internalip import create_app
from internalip.db import get_db, init_db


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app()

    # create the database and load test data
    with app.app_context():
        init_db()

    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
