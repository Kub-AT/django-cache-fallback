==============================================================================
Django Cache Fallback.
==============================================================================
:Info: This is the README file for Django Cache Fallback.
:Author: Jakub Stawowy

.. index: README
.. image:: https://travis-ci.org/Kub-AT/django-cache-fallback.svg?branch=master
   :target: https://travis-ci.org/Kub-AT/django-cache-fallback

PURPOSE
-------
Allows you to set fallback cache backend (multiple cache backend).
The data is not shared between cache backends.
Example: Memcached is not available, backend switch to fallback. Site may slow down (cache have to be set)
but will not rise an error (watch your logs)

INSTALLATION
------------

.. code:: bash

    pip install django-cache-fallback

.. code:: python

    INSTALLED_APPS = (
       ...
       'cache_fallback',
    )

USAGE
-----
Usage example PyLibMCCache + LocMemCache

.. code:: python

    CACHES = {
        'default': {
            'BACKEND': 'cache_fallback.FallbackCache',
        },

        'main_cache': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '/tmp/memcached.sock',
            'TIMEOUT': 500,
        },
        'fallback_cache': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique'
        }

    }
