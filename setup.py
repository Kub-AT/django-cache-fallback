#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass to py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        import django
        from django.conf import settings

        settings.configure(
            TESTING=True,
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': 'test.db'
                },
            },
            CACHES={
                'default': {
                    'BACKEND': 'cache_fallback.FallbackCache',
                },

                'fallback_cache': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                    'LOCATION': 'unique'
                },
                'main_cache': {
                    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
                }

            },
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'cache_fallback',
                'tests.testapp',
            ),
            MIDDLEWARE_CLASSES=('django.middleware.common.CommonMiddleware',),
        )

        if django.VERSION[:2] >= (1, 7):
            django.setup()

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='django-cache-fallback',
    version='0.2.2',
    description='Django Cache Fallback',
    keywords='django-cache-fallback, django cache, multiple cache, fallback cache',
    author='Jakub Stawowy',
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
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=requirements,
    tests_require=[
        'flake8',
        'pytest==4.6.5',  # with python <3.4 support 
        'coverage',
        'pytest-cov',
        'python-memcached',
        'mock',
    ],
    setup_requires=['pytest-runner'],
    cmdclass={'test': PyTest}
)
