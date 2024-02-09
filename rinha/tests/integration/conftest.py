from app.core.infra.db.client import ClientDatabase
from app.database import get_db
from app.main import app
from typing import Callable
from pytest import fixture

from fastapi.testclient import TestClient

from tests.integration.db_config import override_get_db

# app.dependency_overrides[get_db] = override_get_db


@fixture(scope="session")
def build_client() -> TestClient:
    client = TestClient(app)
    return client


@fixture(scope="session")
def build_session():
    db_session = next(override_get_db())
    return db_session


@fixture(scope="session")
def build_client_db(build_session) -> ClientDatabase:
    client_db = ClientDatabase(build_session)
    return client_db