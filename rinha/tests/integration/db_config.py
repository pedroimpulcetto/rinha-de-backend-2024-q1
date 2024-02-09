from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import POSTGRES_URL


# SQLALCHEMY_DATABASE_URL = f"{POSTGRES_URL}/test"

engine = create_engine(POSTGRES_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    connection = engine.connect()
    transaction = connection.begin()
    db = Session(bind=connection)
    yield db
    db.close()
    transaction.rollback()
    connection.close()