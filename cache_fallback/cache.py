# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django.core import signals
from django.core.cache.backends.base import BaseCache

logging.basicConfig()
logger = logging.getLogger(__name__)


def get_cache(backend, **kwargs):
    """
    Compatibilty wrapper for getting Django's cache backend instance

    original source:
    https://github.com/vstoykov/django-imagekit/commit/c26f8a0538778969a64ee471ce99b25a04865a8e
    """
    from django.core import cache

    # Django < 1.7
    if not hasattr(cache, '_create_cache'):
        return cache.get_cache(backend, **kwargs)

    cache = cache._create_cache(backend, **kwargs)
    # Some caches -- python-memcached in particular -- need to do a cleanup at the
    # end of a request cycle. If not implemented in a particular backend
    # cache.close is a no-op. Not available in Django 1.5
    if hasattr(cache, 'close'):
        signals.request_finished.connect(cache.close)
    return cache


class FallbackCache(BaseCache):
    _cache = None
    _cache_fallback = None

    def __init__(self, params=None, *args, **kwargs):
        BaseCache.__init__(self, *args, **kwargs)
        self._cache = get_cache('main_cache')
        self._cache_fallback = get_cache('fallback_cache')

    def _call_with_fallback(self, method, *args, **kwargs):
        try:
            return self._call_main_cache(args, kwargs, method)
        except Exception as e:
            logger.warning('Switch to fallback cache')
            logger.exception(e)
            return self._call_fallback_cache(args, kwargs, method)

    def _call_main_cache(self, args, kwargs, method):
        return getattr(self._cache, method)(*args, **kwargs)

    def _call_fallback_cache(self, args, kwargs, method):
        return getattr(self._cache_fallback, method)(*args, **kwargs)

    def add(self, key, value, timeout=None, version=None):
        return self._call_with_fallback('add', key, value, timeout=timeout, version=version)

    def get(self, key, default=None, version=None):
        return self._call_with_fallback('get', key, default=default, version=version)

    def set(self, key, value, timeout=None, version=None, client=None):
        return self._call_with_fallback('set', key, value, timeout=timeout, version=version)

    def delete(self, key, version=None):
        return self._call_with_fallback('delete', key, version=version)

    def clear(self):
        return self._call_with_fallback('clear')
