import os
import tempfile

import pytest

from application import create_app

# Pytests
@pytest.fixture
def app():
    app = create_app()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()