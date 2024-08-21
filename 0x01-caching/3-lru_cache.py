#!/usr/bin/env python3
"""
LRUCache module that implements a Least Recently Used (LRU) caching system.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that implements a Least Recently Used (LRU) caching system.

    Inherits from BaseCaching and follows the LRU eviction strategy.
    """

    def __init__(self):
        """
        Initialize the LRUCache class.

        Calls the parent class initializer and sets up an order tracking list
        to keep track of the LRU item.
        """
        super().__init__()
        self.lru_order = []

    def put(self, key, item):
        """
        Add an item to the cache using the LRU caching strategy.

        If key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, discard the least recently used item.

        Args:
            key (str): The key to add to the cache.
            item (str): The value to associate with the key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the key from lru_order to update its position later
            self.lru_order.remove(key)

        # Add or update the cache and the LRU tracking order
        self.cache_data[key] = item
        self.lru_order.append(key)

        # Check if we need to evict an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used item
            least_recent_key = self.lru_order.pop(0)
            del self.cache_data[least_recent_key]
            print("DISCARD: {}".format(least_recent_key))

    def get(self, key):
        """
        Get an item by key from the cache.

        If key is None or does not exist in cache_data, return None.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            str: The value linked to the key, or None if key is invalid.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update LRU order since key has been accessed
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]

    def print_cache(self):
        """
        Print the current cache state.
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print("{}: {}".format(key, value))
