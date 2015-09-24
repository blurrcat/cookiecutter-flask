#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


__version__ = '0.1.0'


dependencies = {}
for env in ('prod', 'dev'):
    requires = []
    with open('requirements/{}.txt'.format(env), encoding='utf-8') as f:
        for line in f:
            if not (line.startswith('#') or line.startswith('-r')):
                requires.append(line)
    dependencies[env] = requires


setup(
    name='{{cookiecutter.app}}',
    version=__version__,
    packages=find_packages(),
    install_requires=dependencies['prod'],
    tests_require=dependencies['dev'],
    extras_require={
        'dev': dependencies['dev'],
    }
)
