#!/usr/bin/env python3
""" LFU Cache Module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and an LFU cache """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = {}  # To keep track of item frequencies
        self.lru_order = []  # To keep track of LRU order

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.lru_order.remove(key)
            self.lru_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used item
                lfu_keys = [
                    k for k, v in self.frequency.items()
                    if v == min(self.frequency.values())
                ]
                if len(lfu_keys) > 1:
                    # If there's a tie, use the LRU order to break it
                    lfu_key = next(k for k in self.lru_order if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                # Discard the least frequently used item
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.lru_order.remove(lfu_key)

            # Add the new item and update the frequency and LRU order
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.lru_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
