#!/usr/bin/env python
import sys

import django
from django.conf import settings


settings.configure(
    TESTING=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
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


# Run tests

from django.test.runner import DiscoverRunner  # noqa

test_runner = DiscoverRunner(verbosity=1)
test_runner.setup_databases()
failures = test_runner.run_tests(['tests', ])
if failures:
    sys.exit(failures)
