import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.sql import text

from app.db import SessionLocal, Base


@pytest.fixture(scope='session')
def db_session():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:
        yield session

        session.rollback()

        # truncate all tables
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(text(f'TRUNCATE {table.name} CASCADE;'))
            session.commit()
