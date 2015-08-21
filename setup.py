#!/usr/bin/env python3

from stager.version import get_version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

get_version()

setup(
    name = 'stager',
    version = '0.0.1',
    description = 'the perfect Gentoo installer',
    url = 'https://github.com/gentoo/stager',
    author = 'Matthew Marchese',
    author_email = 'maffblaster@gentoo.org',
    license = 'To be determined...',
    keywords = 'gentoo installer development',
    packages = [''],
    install_requires = [''],
)

setup(**config)