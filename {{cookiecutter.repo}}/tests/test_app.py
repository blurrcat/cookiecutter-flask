#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_home(client):
    r = client.get('/')
    assert r.status_code == 200
