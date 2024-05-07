#!/usr/bin/python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system
    """

    def __init__(self):
        """initilizer"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        put items into cache
        """

        if key and item:
            if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                key_to_remove = self.queue.pop(0)
                print(f'DISCARD: {key_to_remove}')
                del self.cache_data[key_to_remove]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        access cache item
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
