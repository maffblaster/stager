#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'the perfect Gentoo installer',
    'author': 'Matthew Marchese',
    'url': 'https://github.com/gentoo/stager',
    'download_url': 'https://github.com/gentoo/stager',
    'author_email': 'maffblaster@gentoo.org',
    'version': '0.0.01',
    'install_requires': [''],
    'packages': ['stager'],
    'scripts': [],
    'name': 'stager'
}

setup(**config)