# -*- coding: utf-8 -*-
from unittest.mock import patch

from django.core.cache import BaseCache
from django import test

from cache_fallback import FallbackCache


def get_client(**kwargs):
    return FallbackCache(None, kwargs)


class CacheFallbackBasicTestCase(test.TestCase):
    def setUp(self):
        self._sut = get_client()

    def test_client(self):
        self.assertIsInstance(self._sut, FallbackCache)
        self.assertIsInstance(self._sut._cache, BaseCache)
        self.assertIsInstance(self._sut._cache_fallback, BaseCache)

    @patch.object(FallbackCache, "_call_fallback_cache")
    @patch.object(FallbackCache, "_call_main_cache")
    def test_get_maincache(self, maincache_mock, fallback_cache_mock):
        self._sut.get("irrelevent")
        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

    @patch.object(FallbackCache, "_call_fallback_cache")
    @patch.object(FallbackCache, "_call_main_cache")
    def test_set_maincache(self, maincache_mock, fallback_cache_mock):
        self._sut.set("irrelevent", "123", 5)
        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

    @patch.object(FallbackCache, "_call_fallback_cache")
    @patch.object(FallbackCache, "_call_main_cache")
    def test_get_fallbackcache(self, maincache_mock, fallback_cache_mock):
        self._sut.get("irrelevent")
        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

        maincache_mock.side_effect = Exception()
        self._sut.get("irrelevent")
        fallback_cache_mock.assert_called_once()

    @patch.object(FallbackCache, "_call_fallback_cache")
    @patch.object(FallbackCache, "_call_main_cache")
    def test_multiple_get_fallbackcache(self, maincache_mock, fallback_cache_mock):
        self._sut.get("irrelevent")
        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

        maincache_mock.side_effect = Exception()
        keys = ["irrelevent1", "irrelevent2", "irrelevent3"]
        for key in keys:
            self._sut.get(key)
        self.assertEqual(fallback_cache_mock.call_count, len(keys))

    @patch.object(FallbackCache, "_call_fallback_cache")
    @patch.object(FallbackCache, "_call_main_cache")
    def test_set_fallbackcache(self, maincache_mock, fallback_cache_mock):
        self._sut.set("irrelevent", "123", 5)
        maincache_mock.assert_called_once()
        fallback_cache_mock.assert_not_called()

        maincache_mock.side_effect = Exception()
        self._sut.set("irrelevent", "123", 5)
        fallback_cache_mock.assert_called_once()

    @patch("cache_fallback.cache.logger")
    @patch.object(FallbackCache, "_call_main_cache")
    def test_get_fallbackcache_logger(self, maincache_mock, logger_mock):
        maincache_mock.side_effect = Exception()
        self._sut.get("irrelevent")
        logger_mock.warning.assert_called_with("Switch to fallback cache")
        logger_mock.exception.assert_called_once()
