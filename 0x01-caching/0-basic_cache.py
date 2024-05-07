#!/usr/bin/python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basic caching system
    """

    def __int__(self):
        """initilizer"""
        super().__init__()

    def put(self, key, item):
        """
        put items into cache
        """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        access cache item
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
