#!/usr/bin/python

import setuptools

setuptools.setup(
    name='righthook',
    version='0.0.1',
    packages = setuptools.find_packages(exclude=[]),
    install_requires = [
        'django-celery>=3.0',
        ]
    )


