import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "test-secret-key"
DEBUG = True
USE_TZ = False

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "cache_fallback",
    "tests.testapp",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

CACHES = {
    "default": {"BACKEND": "cache_fallback.FallbackCache"},
    "fallback_cache": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique",
    },
    "main_cache": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
}

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]