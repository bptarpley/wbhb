#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='wbhb',
    version='2.0',
    description='Bibliography',
    author='Bryan Tarpley',
    author_email='bptarpley@tamu.edu',
    license='BSD',
    install_requires=[
        'django',
        'mysqlclient'
    ],
    packages=find_packages()
)
