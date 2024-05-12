#!/usr/bin/python3
"""
BasicCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFU caching system
    """

    def __init__(self):
        """initilizer"""
        super().__init__()
        self.queue = []
        self.use_frequency = {}

    def put(self, key, item):
        """
        put items into cache
        """

        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                val = min(self.use_frequency.values())
                for k, v in self.use_frequency.items():
                    if v == val:
                        print(f'DISCARD: {k}')
                        del self.cache_data[k]
                        del self.use_frequency[k]
                        break
            self.queue.append(key)
            self.cache_data[key] = item
            self.use_frequency[key] = self.use_frequency.get(key, 0) + 1

    def get(self, key):
        """
        access cache item
        """
        if key and key in self.cache_data:
            self.use_frequency[key] += 1
            return self.cache_data[key]
        else:
            return None
