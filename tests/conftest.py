#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from manstein.app import create_app


TEST_CONFIG = {
    'DEBUG': True,
    'TESTING': True,
    'SQLALCHEMY_DATABASE_URI': 'sqlite://',
    'WTF_CSRF_ENABLED': False,
}


@pytest.yield_fixture
def app():
    _app = create_app(**TEST_CONFIG)
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()
