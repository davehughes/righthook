#!/usr/bin/python

import setuptools

setuptools.setup(
    name='righthook',
    version='0.0.1',
    packages = setuptools.find_packages(exclude=[]),
    author = 'David Hughes',
    author_email = 'd@vidhughes.com',
    url = 'https://github.com/davehughes/righthook',
    download_url = 'https://github.com/davehughes/righthook/tarball/0.0.1',
    keywords = [
        'Django', 'Celery', 'task', 'queue', 'webhook',
        ],
    install_requires = [
        'django-celery>=3.0',
        ],
    )


