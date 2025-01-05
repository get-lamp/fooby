import pytest
from app import models


def test_write_and_read(db_session):
    user = models.User(name='John', email='john@fooby.com')
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    assert user.id is not None
