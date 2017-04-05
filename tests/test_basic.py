#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mock import patch

from django.core.cache import BaseCache
from django import test

from cache_fallback import FallbackCache


def get_client(**kwargs):
    return FallbackCache(None, kwargs)


class CacheFallbackBasicTestCase(test.TestCase):

    def test_client(self):
        client = get_client()
        self.assertIsInstance(client, FallbackCache)
        self.assertIsInstance(client._cache, BaseCache)
        self.assertIsInstance(client._cache_fallback, BaseCache)

    @patch.object(FallbackCache, '_call_fallback_cache')
    @patch.object(FallbackCache, '_call_main_cache')
    def test_get_maincache(self, maincache_mock, fallback_cache_mock):
        client = get_client()
        client.get('irrelevent')

        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

    @patch.object(FallbackCache, '_call_fallback_cache')
    @patch.object(FallbackCache, '_call_main_cache')
    def test_set_maincache(self, maincache_mock, fallback_cache_mock):
        client = get_client()
        client.set('irrelevent', '123', 5)

        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

    @patch.object(FallbackCache, '_call_fallback_cache')
    @patch.object(FallbackCache, '_call_main_cache')
    def test_get_fallbackcache(self, maincache_mock, fallback_cache_mock):
        client = get_client()
        client.get('irrelevent')

        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

        maincache_mock.side_effect = Exception()
        client.get('irrelevent')

        fallback_cache_mock.assert_called_once()

    @patch.object(FallbackCache, '_call_fallback_cache')
    @patch.object(FallbackCache, '_call_main_cache')
    def test_multiple_get_fallbackcache(self, maincache_mock, fallback_cache_mock):
        client = get_client()
        client.get('irrelevent')

        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

        maincache_mock.side_effect = Exception()
        to_get = ['irrelevent1', 'irrelevent2', 'irrelevent3']
        for key in to_get:
            client.get(key)

        fallback_cache_mock.assert_called()
        self.assertEqual(fallback_cache_mock.call_count, len(to_get))

    @patch.object(FallbackCache, '_call_fallback_cache')
    @patch.object(FallbackCache, '_call_main_cache')
    def test_set_fallbackcache(self, maincache_mock, fallback_cache_mock):
        client = get_client()
        client.set('irrelevent', '123', 5)

        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

        maincache_mock.side_effect = Exception()
        client.set('irrelevent', '123', 5)

        fallback_cache_mock.assert_called_once()

    @patch('cache_fallback.cache.logger')
    @patch.object(FallbackCache, '_call_main_cache')
    def test_get_fallbackcache_logger(self, maincache_mock, logger_mock):
        client = get_client()
        maincache_mock.side_effect = Exception()
        client.get('irrelevent')

        logger_mock.warning.assert_called_with('Switch to fallback cache')
        logger_mock.exception.assert_called_once()
