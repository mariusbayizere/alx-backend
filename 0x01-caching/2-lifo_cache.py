#!/usr/bin/env python3
""" LIFO Cache Module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching and LIFO cache """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.last_key = None  # To keep track of the last item added

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                # Discard the last item put in cache
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]

        # Add the item and update the last_key
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """ Get an item from the cache """
        return self.cache_data.get(key, None)
