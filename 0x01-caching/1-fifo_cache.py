#!/usr/bin/env python3
""" FIFO Cache Module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching and FIFO cache """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.queue = []  # To keep track of the order of insertion

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the first item put in cache (FIFO)
            fifo_key = self.queue.pop(0)
            del self.cache_data[fifo_key]
            print(f"DISCARD: {fifo_key}")

        # Add the item and update the queue
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get an item from the cache """
        return self.cache_data.get(key, None)
