#!/usr/bin/env python3
"""
MRUCache module that implements a Most Recently Used (MRU) caching system.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that implements a Most Recently Used (MRU) caching system.

    Inherits from BaseCaching and follows the MRU eviction strategy.
    """

    def __init__(self):
        """
        Initialize the MRUCache class.

        Calls the parent class initializer and sets up an order tracking list
        to keep track of the MRU item.
        """
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """
        Add an item to the cache using the MRU caching strategy.

        If key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, discard the most recently used item.

        Args:
            key (str): The key to add to the cache.
            item (str): The value to associate with the key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the key from mru_order to update its position later
            self.mru_order.remove(key)

        # Add or update the cache and the MRU tracking order
        self.cache_data[key] = item
        self.mru_order.append(key)

        # Check if we need to evict an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the most recently used item before the last inserted one
            most_recent_key = self.mru_order.pop(-2)
            del self.cache_data[most_recent_key]
            print("DISCARD: {}".format(most_recent_key))

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

        # Update MRU order since key has been accessed
        self.mru_order.remove(key)
        self.mru_order.append(key)

        return self.cache_data[key]

    def print_cache(self):
        """
        Print the current cache state.
        """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print("{}: {}".format(key, value))
