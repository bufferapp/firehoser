#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

requirements = [
    'click',
    'boto3'
]

setup(
    name="firehoser",
    version='0.5.1',
    py_modules=['firehoser'],
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'firehoser=firehoser.cli:firehoser'
        ]
    }
)
