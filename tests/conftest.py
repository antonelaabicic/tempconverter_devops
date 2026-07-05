import pytest, os

os.environ.setdefault("DB_USER", "user")
os.environ.setdefault("DB_PASS", "password")
os.environ.setdefault("DB_HOST", "localhost")
os.environ.setdefault("DB_NAME", "tempconverter")

os.environ.setdefault("STUDENT", "Antonela Abicic")
os.environ.setdefault("COLLEGE", "Algebra University College")

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        with app.test_client() as client:
            yield client