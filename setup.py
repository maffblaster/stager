#!/usr/bin/env python3

import os
from stager.stager import __author__, __email__, __description__, __source__, __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    author=__author__,
    author_email=__email__,
    name='stager',
    version=__version__,
    description=__description__,
    url=__source__,
    license='MIT',
    keywords='gentoo installer',
    packages=['stager'],
    install_requires=['flask, docopt'],
    long_description=read('readme.md'),
    py_modules=['stager'],
)
