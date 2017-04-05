#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cache_fallback
import cache_fallback.cache


def test_true():
    """Test if True is truthy."""
    assert True


def test_import():
    """Test imports."""
    cache_fallback
    cache_fallback.cache
