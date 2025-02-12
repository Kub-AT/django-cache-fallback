#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages

with io.open("requirements.txt", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip()]

with io.open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-cache-fallback",
    version="0.4.0",
    description="Django Cache Fallback",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Jakub Stawowy",
    author_email="Kub-AT@users.noreply.github.com",
    url="https://github.com/Kub-AT/django-cache-fallback",
    license="3-clause BSD",
    platforms="any",
    zip_safe=False,
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest",
            "coverage",
            "pytest-cov",
            "flake8",
            "python-memcached",
            "mock",
            "django",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
    setup_requires=["tox"],
)