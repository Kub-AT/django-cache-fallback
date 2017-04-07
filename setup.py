#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import io
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]


setup(
    name='django-cache-fallback',
    version='0.2.1',
    description='Django Cache Fallback',
    keywords='django-cache-fallback, django cache, multiple cache, fallback cache',
    author='Jakub S',
    author_email='Kub-AT@users.noreply.github.com',
    url='https://github.com/Kub-AT/django-cache-fallback',
    license='3-clause BSD',
    long_description=io.open('./README.rst', 'r', encoding='utf-8').read(),
    platforms='any',
    zip_safe=False,
    classifiers=[
                'Programming Language :: Python',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Development Status :: 5 - Production/Stable',
                'Environment :: Web Environment',
                'Framework :: Django',
                'Framework :: Django :: 1.11',
                'Framework :: Django :: 1.10',
                'Framework :: Django :: 1.9',
                'Framework :: Django :: 1.8',
                'Intended Audience :: Developers'
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=requirements,
)
