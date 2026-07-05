import pytest, os

os.environ["DB_USER"] = "user"
os.environ["DB_PASS"] = "password"
os.environ["DB_HOST"] = "localhost"
os.environ["DB_NAME"] = "tempconverter"

os.environ["STUDENT"] = "Antonela Abicic"
os.environ["COLLEGE"] = "Algebra University College"

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        with app.test_client() as client:
            yield client