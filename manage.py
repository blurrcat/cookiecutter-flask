#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager, Shell
from manstein.app import create_app

app = create_app()
manager = Manager(app)


def _make_context():
    return {
        'app': app,
    }

@manager.command
def urls(prefix=''):
    rules = sorted(
        rule.rule for rule in app.url_map._rules
        if rule.rule.startswith(prefix))
    for r in rules:
        print(r)


manager.add_command('shell', Shell(make_context=_make_context))


if __name__ == '__main__':
    manager.run()

