import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Use SQLite in-memory database for tests
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as c:
        # Create a test user
        c.post(
            "/api/v1/users/",
            json={
                "email": "test@example.com",
                "username": "testuser",
                "password": "testpass123",
            },
        )
        # Login to get token
        response = c.post(
            "/api/v1/auth/login",
            data={"username": "test@example.com", "password": "testpass123"},
        )
        token = response.json()["access_token"]
        c.headers.update({"Authorization": f"Bearer {token}"})
        yield c
