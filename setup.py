#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import io
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]


setup(
    name='django-cache-fallback',
    version='0.2.0',
    description='Django Cache Fallback',
    keywords='django-cache-fallback, django cache, multiple cache, fallback cache',
    author='Jakub S',
    author_email='@',
    url='https://github.com/Kub-AT/django-cache-fallback',
    license='3-clause BSD',
    long_description=io.open('./README.rst', 'r', encoding='utf-8').read(),
    platforms='any',
    zip_safe=False,
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    # 'Development Status :: 4 - Beta',
    classifiers=[
                'Programming Language :: Python',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=requirements,
)
