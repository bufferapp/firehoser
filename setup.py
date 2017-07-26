#!/usr/bin/env python

from setuptools import setup

requirements = [
    'click',
    'boto3'
]

setup(
    name="firehoser",
    version='0.5.1',
    py_modules=['firehoser'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'firehoser=firehoser.cli:firehoser'
        ]
    }
)
