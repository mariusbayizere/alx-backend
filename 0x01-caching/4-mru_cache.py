#!/usr/bin/env python3
"""
Module for implementing a MRU caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that implements a Most Recently Used (MRU) caching system.
    Inherits from BaseCaching and follows MRU eviction strategy.
    """

    def __init__(self):
        """
        Initialize the MRUCache class.
        Call the parent class initializer and set up an order tracking list.
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Add an item in the cache using the MRU caching strategy.
        If the cache exceeds MAX_ITEMS, the most recently used discarded.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)

        self.cache_data[key] = item
        self.mru_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recent_key = self.mru_order.pop(-2)
            del self.cache_data[most_recent_key]
            print("DISCARD: {}".format(most_recent_key))

    def get(self, key):
        """
        Get an item by key from the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update MRU order since key has been accessed
        self.mru_order.remove(key)
        self.mru_order.append(key)

        return self.cache_data[key]

    def print_cache(self):
        """
        Print the current state of the cache.
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print("{}: {}".format(key, value))
