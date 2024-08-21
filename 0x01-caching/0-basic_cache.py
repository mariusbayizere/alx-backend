#!/usr/bin/env python3
"""
This module contains the BasicCache class which implements
a simple cache system with no limit.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that implements a caching system with no limit.
    Inherits from BaseCaching.
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        Args:
            key: Key to store the item.
            item: Item to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache.
        Args:
            key: Key of the item to retrieve.
        Returns:
            The item associated with the key.
        """
        return self.cache_data.get(key, None)
