#!/usr/bin/env python3
"""Task 2 Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching and
    is a caching system
    """
    def __init__(self):
        """Initializes the LIFOCache class.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds a item to the caching system
        """
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                last = self.keys.pop()
                print("DISCARD: {}".format(last))
                del self.cache_data[last]
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Gets a value from the caching system
        """
        return self.cache_data.get(key)
